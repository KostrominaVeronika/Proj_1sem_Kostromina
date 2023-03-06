''' Функция вычисляет пепиметр и площадь квадрата '''
__all__ = ['s_perimetr', 's_area']

default_a = 15


def s_perimetr(a=default_a):
    p = 4 * a
    return p


def s_area(a=default_a):
    s = a * a
    return s