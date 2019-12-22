# -*- coding: utf-8 -*-
"""Тесты проекта"""


import unittest
import json
import json2xlsx


class TestParsing(unittest.TestCase):
    def test_incorrect_filename(self):
        """Тест на некоректное имя файла"""
        with self.assertRaises(FileNotFoundError):
            json2xlsx.load_data("this is incorrect name of file.txt")

    def test_incorrect_file(self):
        """Тест на некорректный тип файла"""
        with self.assertRaises(json.decoder.JSONDecodeError):
            json2xlsx.load_data("./incorrect_file.txt")

    def test_teachers_none(self):
        teachers = json2xlsx.parse_teachers([])
        self.assertEqual(teachers, None)

    # def test_teachers_common(self):
    #     teachers: tuple = json2xlsx.parse_teachers([['NAME', ['7335'], '122', True]])
    #     attributes = ['NAME', ['7335'], '122', True]
    #     teacher_test = json2xlsx.Teacher(attributes[0], attributes[1:])
    #     self.assertEqual(teacher_test, teachers[0])

    def test_teachers_wrong(self):
        teachers: tuple = json2xlsx.parse_teachers([['NAME', [], '122', True]])
        attributes = ['NAME', ['7335'], '122', True]
        teacher_test = json2xlsx.Teacher(attributes[0], attributes[1:])
        self.assertNotEqual(teacher_test, teachers[0])
        self.assertNotEqual(teacher_test, "str")

    def test_notes_none(self):
        notes = json2xlsx.parse_notes({'1': [], '2': [], '3': [], '4': []})
        self.assertEqual(notes, None)

    # def test_notes_common(self):
    #     attributes = {
    #         '1':[['Name1', ['7111'], '122', True],['Name2', ['7112'], '123', False]],
    #         '2':[['FIO', ['7336'], '166', True]],
    #         '3':[['NAME', [], '155', False]],
    #         '4':[]
    #     }
    #     notes = json2xlsx.parse_notes(attributes)
    #     for key in attributes.keys():
    #         if int(key) > len(notes): break
    #         note = json2xlsx.Note(key, json2xlsx.parse_teachers(attributes[key]))
    #         self.assertEqual(note, notes[int(key)-1])

    def test_notes_wrong(self):
        attributes = {
            '1': [['Name1', ['7111'], '122', True], ['Name2', ['7112'], '123', False]],
            '2': [['FIO', ['7336'], '166', True]],
            '3': [['NAME', [], '155', False]],
            '4': []
        }

        notes = json2xlsx.parse_notes(attributes)
        self.assertNotEqual(notes, "str")


if __name__ == '__main__':
    unittest.main()
