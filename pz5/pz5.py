"""Draw figures: circle, oval and square"""
from abc import ABC, abstractmethod


class Figure(ABC):
    """Abstract class"""
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def draw(self):
        """Figure"""

    def pylint(self):
        """For pylint"""
        print(self.size)


class Circle(Figure):
    """Circle"""

    def __init__(self, size):
        Figure.__init__(self, size)
        self.name = 'Circle'

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Figure {0}".format(self.name)

    def draw(self):
        """draw circle"""
        # if self.size < 5 or self.size > 10:
        print(' ' * (self.size + 3) + '*  ' * (self.size//2), end='')
        print()
        print(' ' * (self.size//2) + ' *' + ' ' * self.size
              + ' ' * (self.size//2 + self.size//2 + self.size//2) + '*', end='')
        print()
        print(' ' * (self.size // 2 - 3) + ' *' + ' ' * (self.size + 3)
              + ' ' * (self.size // 2 + self.size//2 + self.size//2 + 2) + '*', end='')
        print()
        for _ in range(self.size//2 + 1):
            print('*', end='')
            for _ in range(int(self.size) * 3 + self.size//2 + 1):
                print(' ', end='')
            print('*')
        print(end='')
        print(' ' * (self.size // 2 - 3) + ' *' + ' ' * (self.size + 3)
              + ' ' * (self.size // 2 + self.size // 2 + self.size // 2 + 2) + '*', end='')
        print()
        print(' ' * (self.size // 2) + ' *' + ' ' * self.size
              + ' ' * (self.size // 2 + self.size // 2 + self.size // 2) + '*', end='')
        print()
        print(' ' * (self.size + 3) + '*  ' * (self.size // 2), end='')
        print()
        # else:
        #     print('  ', end='')
        #     for _ in range(self.size + 1):
        #         print('*', end='  ')
        #     print()
        #     print(' ', end='')
        #     print('*', end='')
        #     for _ in range(int(self.size) * 3 + 1):
        #         print(' ', end='')
        #     print('*', end='')
        #     print()
        #     for _ in range(self.size):
        #         print('*', end='')
        #         for _ in range(int(self.size) * 3 + 3):
        #             print(' ', end='')
        #         print('*')
        #     print(' ', end='')
        #     print('*', end='')
        #     for _ in range(int(self.size) * 3 + 1):
        #         print(' ', end='')
        #     print('*', end='')
        #     print()
        #     print('  ', end='')
        #     for _ in range(self.size + 1):
        #         print('*', end='  ')
        #     print()


class Oval(Figure):
    """Oval"""
    def __init__(self, size):
        Figure.__init__(self, size)
        self.name = 'Oval'

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Figure {0}".format(self.name)

    def draw(self):
        # if self.size < 5 or self.size > 10:
        print('\n' + ' ' * (self.size + 3) + '*  ' * (self.size // 2), end='')
        print()
        print(' ' * (self.size // 2) + ' *' + ' ' * self.size
              + ' ' * (self.size // 2 + self.size // 2 + self.size // 2) + '*', end='')
        print()
        print(' ' * (self.size // 2 - 3) + ' *' + ' ' * (self.size + 3)
              + ' ' * (self.size // 2 + self.size // 2 + self.size // 2 + 2) + '*', end='')
        print()
        for _ in range(self.size // 2 + self.size * 3):
            print('*', end='')
            for _ in range(int(self.size) * 3 + self.size // 2 + 1):
                print(' ', end='')
            print('*')
        print(end='')
        print(' ' * (self.size // 2 - 3) + ' *' + ' ' * (self.size + 3)
              + ' ' * (self.size // 2 + self.size // 2 + self.size // 2 + 2) + '*', end='')
        print()
        print(' ' * (self.size // 2) + ' *' + ' ' * self.size
              + ' ' * (self.size // 2 + self.size // 2 + self.size // 2) + '*', end='')
        print()
        print(' ' * (self.size + 3) + '*  ' * (self.size // 2), end='')
        print()
        # else:
        #     print('  ', end='')
        #     for _ in range(self.size + 1):
        #         print('*', end='  ')
        #     print()
        #     print(' ', end='')
        #     print('*', end='')
        #     for _ in range(int(self.size) * 3 + 1):
        #         print(' ', end='')
        #     print('*', end='')
        #     print()
        #     for _ in range(self.size):
        #         print('*', end='')
        #         for _ in range(int(self.size) * 3 + 3):
        #             print(' ', end='')
        #         print('*')
        #     print(' ', end='')
        #     print('*', end='')
        #     for _ in range(int(self.size) * 3 + 1):
        #         print(' ', end='')
        #     print('*', end='')
        #     print()
        #     print('  ', end='')
        #     for _ in range(self.size + 1):
        #         print('*', end='  ')
        #     print()


class Square(Figure):
    """Square"""
    def __init__(self, size):
        Figure.__init__(self, size)
        self.name = 'Square'

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Figure {0}".format(self.name)

    def draw(self):
        """draw square"""
        print('\n*' + '*' * (self.size * 3), end='*')
        for _ in range(self.size//2 * 2, 1, -1):
            print('\n*' + ' ' * (self.size * 3) + '*', end='')
        print('\n*' + '*' * (self.size * 3) + '*')


if __name__ == "__main__":
    CIRCLE = Circle(6)
    OVAL = Oval(6)
    SQUARE = Square(6)

    print(CIRCLE)
    print(OVAL)
    print(SQUARE, '\n')

    FIGURES = [CIRCLE, OVAL, SQUARE]
    print(FIGURES, '\n')

    CIRCLE.draw()
    OVAL.draw()
    SQUARE.draw()
