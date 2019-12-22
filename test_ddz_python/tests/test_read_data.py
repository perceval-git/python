"""Test for the load module"""
import unittest
import json
import src.data_json as dj


class LoadDataTest(unittest.TestCase):
    def test_incorrect_filename(self):
        with self.assertRaises(FileNotFoundError):
            dj.load_data('this is incorrect filename.txt')

    def test_incorrect_file(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            dj.load_data('./tests/tests_resources/data.txt')


if __name__ == '__main__':
    unittest.main()
