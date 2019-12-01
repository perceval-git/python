# -*- coding: utf-8 -*-
"""
tests for Guesser
"""


import unittest
import sys
import io
from unittest.mock import patch
from pz4.pz4 import Guesser


class TestGuesser(unittest.TestCase):
    """test_case for Guesser"""
    def test_check(self):
        rnd = 50
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = [50, 90, 10]
        should_ans = [0, 1, -1]
        for i in range(len(guess)):
             self.assertEqual(guesser.check(guess[i]), should_ans[i])

    def test_play(self):
        rnd = 50
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = [10, 90, 50]
        should_ans = 'Бери выше Бери ниже  Успех! Верно угадано число {0}'.format(rnd)
        with patch('builtins.input', side_effect=guess):
            capt_out = io.StringIO()
            sys.stdout = capt_out
            guesser.play()
            sys.stdout = sys.__stdout__
            self.assertEqual(capt_out.getvalue().strip().replace('\n', ' '), should_ans)

    def test_play_error(self):
        rnd = 15
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        should_ans = ['Test_string']
        with patch('builtins.input', side_effect=should_ans):
            self.assertRaises(ValueError, guesser.play)

    def test_play_exit(self):
        with patch('builtins.input', return_value='exit'):
            guess = Guesser()
            self.assertEqual(guess.play(), None)


if __name__ == '__main__':
    unittest.main()
