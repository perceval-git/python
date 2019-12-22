from random import choice
from string import ascii_letters
n = input('Введите необхожимое количество символов:')
print(''.join(choice(ascii_letters) for _ in range(int(n))))
