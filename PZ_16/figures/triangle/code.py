__all__ = ['t_area', 't_perimetr']

import math

default_a = 7
default_b = 2
default_c = 8


def t_perimetr(a=default_a, b=default_b, c=default_c):
    p = a + b + c
    return p


def t_area(a=default_a, b=default_b, c=default_c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

print(t_area())