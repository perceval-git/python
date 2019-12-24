# -*- coding: utf-8 -*-
"""Тесты проекта"""


import unittest
import json
import json2xlsx


# python3 -m  unittest test_json2xlsx.py
# python3 -m coverage report -m json2xlsx.py
# Тестирование файла с основным кодом (json2xlsx.py) стоит проводить на строках с 1 по 125, по причине того,
# что ниже идет код, отвечающий за запись в таблицу. Выше же код получения данных из json-файла и преобразования его
# в удобный для записи вид.
class TestParsing(unittest.TestCase):
    def test_incorrect_filename(self):
        """Тест на несуществующее имя файла"""
        with self.assertRaises(FileNotFoundError):
            json2xlsx.load_data("this is nonexistent name of file.txt")

    def test_incorrect_file(self):
        """Тест на некорректный тип файла"""
        with self.assertRaises(json.decoder.JSONDecodeError):
            json2xlsx.load_data("./incorrect_file.txt")

    # def test_file_none(self):
    #     with json2xlsx.load_data("empty.json"):
    #         json2xlsx.load_data(json.load(self))
    #
    # def test_file_exist(self):
    #     with open("test_readable.json") as file:
    #         self.assertIsNone(json.load(file))

    def test_notes_none(self):
        notes = json2xlsx.parse_notes({'1': [], '2': [], '3': [], '4': []})
        self.assertIsNone(notes)

    def test_teachers_none(self):
        teachers = json2xlsx.parse_teachers([])
        self.assertIsNone(teachers)

    def test_teachers_wrong(self):
        teachers: tuple = json2xlsx.parse_teachers([['NAME', [], '122', True]])
        attributes = ['NAME', ['7335'], '122', True]
        teacher_test = json2xlsx.Teacher(attributes[0], attributes[1:])
        self.assertNotEqual(teacher_test, teachers[0])
        self.assertNotEqual(teacher_test, "str")

    def test_notes_none(self):
        notes = json2xlsx.parse_notes({'1': [], '2': [], '3': [], '4': []})
        self.assertIsNone(notes)

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
