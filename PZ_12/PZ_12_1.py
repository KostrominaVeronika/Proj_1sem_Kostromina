''' Проверить есть ли в последовательности N чисел число K'''

import random

try: # ОБработка ошибок ввода
    K = int(input('Введите число: '))
    N = int(input('Введите размер списка: '))
except ValueError:
    print('Вводите числа!')

# Заполнение списка значениями и вывод найденного числа, которое равно, введенному пользователем числу
spisok = [random.randint(1, 100) for i in range(N)]
check = [i for i in spisok if i == K]
print('Число в последовательности', list(set(check)), 'Сколько раз попалось', len(check))
