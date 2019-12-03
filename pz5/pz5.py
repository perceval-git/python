"""Draw figures"""
from abc import ABC, abstractmethod


class Figure(ABC):
    """Abstract class"""
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def draw(self):
        """Figure"""

    def pylint(self):
        """So pylint doesn't swear"""
        print(self.size)


class Circle(Figure):
    """Draw circle"""

    def __init__(self, size):
        Figure.__init__(self, size)
        self.name = 'Circle'

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Figure {0}".format(self.name)

    def draw(self):
        """Circle"""
        print(' ' * (self.size // 4 + 2) + '_' * self.size, end='')
        print('\n' + ' ' * (self.size // 4) + '/' + ' ' * self.size + '  ' + '\\', end='')
        for i, j in zip(reversed(range(self.size // 4 - 1)), range(1, self.size // 4)):
            print('\n' + ' ' * (i + 1) + '/' +
                  ' ' * self.size + '  ' + '  ' * j + '\\', end='')
        print(('\n|' + ' ' * (2 * (self.size // 4) + self.size + 2) + '|')
              * (self.size // 4), end='')
        if self.size < 4:
            print('\n' + '\\' + ' ' + '_' * self.size + ' ' + '/', end='')
        for i, j in zip(reversed(range(self.size // 4)), range(self.size // 4)):
            if i != 0:
                print('\n' + ' ' * (j + 1) + '\\' + ' ' * self.size + '  ' + '  ' * i + '/', end='')
            else:
                print('\n' + ' ' * (j + 1) + '\\' +
                      ' ' + '_' * self.size + ' ' + '  ' * i + '/', end='')
        print()


class Oval(Figure):
    """Draw oval"""
    def __init__(self, size):
        Figure.__init__(self, size)
        self.name = 'Oval'

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Figure {0}".format(self.name)

    def draw(self):
        """Oval"""
        if self.size < 4:
            print(' ', end='')
        print(' ' * (self.size // 4 + 2) + '_' * self.size, end='')
        print('\n' + ' ' + ' ' * (self.size // 4 - 1) + '/' + ' ' * self.size + '  ' + '\\', end='')
        for i, j in zip(reversed(range(self.size // 4 - 1)), range(1, self.size // 4)):
            print('\n' + ' ' * (i + 1) + '/' +
                  ' ' * self.size + '  ' + '  ' * j + '\\', end='')
        if self.size < 4:
            print(('\n|' + ' ' * (2 * (self.size // 4) + self.size + 2) + '  |') *
                  self.size * 3, end='')
        else:
            print(('\n|' + ' ' * (2 * (self.size // 4) + self.size + 2) + '|') *
                  self.size * 3, end='')
        if self.size < 4:
            print('\n' + ' \\' + ' ' + '_' * self.size + ' ' + '/', end='')
        for i, j in zip(reversed(range(self.size // 4)), range(self.size // 4)):
            if i != 0:
                print('\n' + ' ' * (j + 1) + '\\' + ' ' * self.size + '  ' + '  ' * i + '/', end='')
            else:
                print('\n' + ' ' * (j + 1) + '\\' +
                      ' ' + '_' * self.size + ' ' + '  ' * i + '/', end='')
        print()


class Square(Figure):
    """Draw square"""
    def __init__(self, size):
        Figure.__init__(self, size)
        self.name = 'Square'

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Figure {0}".format(self.name)

    def draw(self):
        """Square"""
        print(' ' + '_' * self.size, end='')
        for i in range(self.size//2, 1, -1):
            print('\n|' + ' '*self.size + '|', end='')
        print('\n|' + '_'*self.size + '|')


if __name__ == "__main__":
    OVAL = Oval(11)
    CIRCLE = Circle(11)
    SQUARE = Square(11)

    print(OVAL)
    print(CIRCLE)
    print(SQUARE)

    FIGURES = [OVAL, CIRCLE, SQUARE]
    print(FIGURES)

    # OVAL.draw()
    # CIRCLE.draw()
    # SQUARE.draw()
