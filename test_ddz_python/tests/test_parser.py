"""Test for the parser module"""

import unittest
import src.parser as parser
from src.data_json import load_data

class ParserTest(unittest.TestCase):
    def test_parse_teachers_none(self):
        teachers = parser.parse_teachers([])
        self.assertEqual(teachers, None)

    def test_parse_teachers_common(self):
        teachers: tuple = parser.parse_teachers([['NAME', ['7335'], '122', True]])
        attributes = ['NAME', ['7335'], '122', True]
        teacher_test = parser.Teacher(attributes[0], attributes[1:])
        self.assertEqual(teacher_test, teachers[0])

    def test_parse_teachers_wrong(self):
        teachers: tuple = parser.parse_teachers([['NAME', [], '122', True]])
        attributes = ['NAME', ['7335'], '122', True]
        teacher_test = parser.Teacher(attributes[0], attributes[1:])
        self.assertNotEqual(teacher_test, teachers[0])
        self.assertNotEqual(teacher_test, "str")

    def test_parse_notes_none(self):
        notes = parser.parse_notes({'1':[], '2':[], '3':[], '4':[]})
        self.assertEqual(notes, None)

    def test_parse_notes_common(self):
        attributes = {
            '1':[['Name1', ['7111'], '122', True],['Name2', ['7112'], '123', False]],
            '2':[['FIO', ['7336'], '166', True]],
            '3':[['NAME', [], '155', False]],
            '4':[]
        }

        notes = parser.parse_notes(attributes)
        for key in attributes.keys():
            if int(key) > len(notes): break
            note = parser.Note(key, parser.parse_teachers(attributes[key]))
            self.assertEqual(note, notes[int(key)-1])

    def test_parse_notes_wrong(self):
        attributes1 = {
            '1': [['Name1', ['7111'], '122', True], ['Name2', ['7112'], '123', False]],
            '2': [['FIO', ['7336'], '166', True]],
            '3': [['NAME', [], '155', False]],
            '4': []
        }
        attributes2 = {
            '2': [['Name1', ['7111'], '122', True], ['Name2', ['7112'], '123', False]],
            '3': [['NAME', [], '155', False]],
            '4': []
        }

        notes1 = parser.parse_notes(attributes1)
        notes2 = parser.parse_notes(attributes2)
        self.assertNotEqual(notes1, notes2)
        self.assertNotEqual(notes1, "str")
