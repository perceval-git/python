# -*- coding: utf-8 -*-
"""
calc and Guesser
"""

import random


# def calc(number_1, number_2, operation):
#     """
#     Калькулятор
#     """
#     operations = {
#         '+': int.__add__,
#         '*': int.__mul__,
#         '-': int.__sub__,
#         '/': int.__truediv__
#     }
#
#     if not isinstance(number_1, int) or not isinstance(number_2, int):
#         raise ValueError("Введенные числа не являются целыми")
#
#     if operation not in operations:
#         raise ValueError("Такой операции не существует")
#     operator = operations.get(operation)
#     return operator(number_1, number_2)


class Guesser:
    """Play a 'guess a number' game"""

    def __init__(self):
        """Init a random number for guesser"""
        self.rnd = random.randint(0, 100)

    def check(self, guess):
        """Check if guess was right
        Args:
            guess: str from user that guess a number

        Returns:
            0 if correct
            1 if guess > self.rnd
            -1 if guess < self.rnd

        Raises:
            ValueError: if guess cant be converted to int.
        """
        if guess == self.rnd:
            return 0
        if guess > self.rnd:
            return 1
        return -1

    def play(self):
        """Start a guess game"""
        while True:
            answer = input('Угадайте число: ')
            if answer == 'exit':
                break
            # try:
            answer = int(answer)
            # except ValueError:
            #     print("Вы ввели не число")
            #     continue
            check = self.check(answer)
            if check == 1:
                print('Бери ниже')
            elif check == -1:
                print('Бери выше')
            elif not check:
                print('\nУспех! Верно угадано число {0}'.format(self.rnd))
                break
            else:
                print('Что-то сломалось')


def main():
    """
    Можно было обойтись и без этого, но так pylint не будет ругаться
    """
    guesser = Guesser()
    guesser.play()

if __name__ == '__main__':
    main()
