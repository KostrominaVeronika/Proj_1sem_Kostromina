''' Расчет длины окружности и пириметра '''
__all__ = ['c_area', 'c_perimetr']

import math

default_r = 5


def c_perimetr(r=default_r, pi=math.pi):
    p = 2 * pi * r
    return p


def c_area(r=default_r, pi=math.pi):
    s = pi * math.pow(r, 2)
    return s