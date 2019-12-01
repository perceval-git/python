import random

def shout_on_me():
    sh_str = input('Что ты сказал?!\n')
    while sh_str != 'exit':
        print('Сам ты %s. И не кричи на меня!' % sh_str.upper())
        sh_str = input('Что ты сказал?!\n')

def calc_plus():
    while True:
        term = input('Введите выражение: ')
        if term == "exit":
            break
        list = term.split('+')
        number = len(list)
        try:
            first = list[0]
            second = list[1]
            if first.isdigit() == True and second.isdigit() == True and number == 2:
                print(int(first) + int(second))
            else:
                print('Введено некорретктное выражение, попробуйте еще раз')
        except IndexError:
            print('Введено некорретктное выражение, попробуйте еще раз')

def guessing_game():
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
        elif answer == 'exit':
            print (number)
            break
        else: print('Это не число')

def main():
    t = ('Выберите и введите название программы:\n'
                   '1. Угадайка\n'
                   '2. Покричи\n'
                   '3. Калькулятор \n')
    while True:
        answer = input(t)
        if answer.upper() == 'УГАДАЙКА':
            guessing_game()
        elif answer.upper() == 'ПОКРИЧИ':
            shout_on_me()
        elif answer.upper() == 'КАЛЬКУЛЯТОР':
            calc_plus()
        elif answer == "exit":
            break
        else:
            print('Некорректное название программы.\n')
if __name__ == '__main__':
    main()