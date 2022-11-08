from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculatesquareroot(number):
    """Five sqrt."""
    return sqrt(number)


def calc(your_number):
    """Give sart from your int."""
    if your_number <= 0:
        yu_arg = calculatesquareroot(your_number)
        return (f'Мы вычислили квадратный корень из '
                f'введённого вами числа. Это будет: '
                f'{yu_arg}')
    return ('Nety')


calc(25.5)
