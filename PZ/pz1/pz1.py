import random

def main():
    number = random.randint(0, 10)
    while True:
        answer = input('Угадайте число: ')
        if answer.isdigit():
            answer = int(answer)

            if answer == number:
                print('Успех')
                break

            elif answer < number:
                print('Бери выше')
            else:
                print('Бери ниже')

        elif answer == 'exit':
            print (number)
            return 0
        else: print('Это не число')

if __name__ == '__main__':
    main();
