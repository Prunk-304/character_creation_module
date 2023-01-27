from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(Num):
    """Вычисляет квадратный корень."""
    return sqrt(Num)


def calc(your_number):
    """Печать результата вычислений."""
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {calculate_square_root(your_number)}')


print(message)
calc(25.5)
