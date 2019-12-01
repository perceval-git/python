"""PZ3"""

import random


def shout_on_me():
    """Покричи на меня"""
    while True:
        sh_str = input('Что ты сказал?!')
        if sh_str == 'q' or sh_str == 'exit':
            return sh_str
        else:
            print('Сам ты %s. И не кричи на меня!' % sh_str.upper())


def calc_plus():
    """Калькулятор"""
    while True:
        term = input('Введите выражение: ')
        if term == 'q' or term == 'exit':
            return term
        number = term.split('+')
        try:
            first = number[0]
            second = number[1]
            print(int(first) + int(second))
        except IndexError:
            print('Введено некорректное выражение, попробуйте еще раз')


def guessing_game():
    """Угадайка"""
    number = random.randint(0, 10)
    while True:
        answer = input('Угадайте число: ')
        if answer.isdigit():
            answer = int(answer)
            if answer == number:
                print('Успех')
                return 'Успех'
            elif answer < number:
                print('Бери выше')
            else:
                print('Бери ниже')
        elif answer == 'q' or answer == 'exit':
            print(number)
            return answer
        else: print('Это не число')


def print_menu():
    """Меню"""
    print("1. Угадайка\n2. Покричи\n3. Калькулятор")


def main():
    """Выполненеие всей программы"""
    dict_funcs = {'УГАДАЙКА': guessing_game, 'ПОКРИЧИ': shout_on_me, 'КАЛЬКУЛЯТОР': calc_plus}
    num = dict(enumerate(dict_funcs.keys()))
    print_menu()
    while True:
        answer = input('Выберите и введите название/номер программы:')
        if answer == 'exit':
            return
        elif answer.isdigit():
            try:
                answer = num[int(answer) - 1]
            except KeyError:
                print("Введена несуществующая функция ")
                continue
        else:
            answer = answer.upper()
        try:
            answer_out = dict_funcs.get(answer)()
            if answer_out == 'exit':
                print("Завершена программа", answer)
                break
            elif answer_out == 'q':
                print_menu()
        except TypeError:
            print("Введена несуществующая функция ")


if __name__ == '__main__':
    main()
