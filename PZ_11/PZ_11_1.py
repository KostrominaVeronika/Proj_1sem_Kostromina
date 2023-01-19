# Задача 1
'''Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов'''

import random

# Создаю файл и записываю в него случайные цифры
file_num = open('numbers.txt', 'w')
for i in range(14):
  file_num.write(str(random.randint(-10, 10)) + ' ')
file_num.close()

# Читаю раннее созданный файл и подготавливаю его к работе, как список
file_num2 = open('numbers.txt')
numbers = file_num2.read()
numbers_split = numbers.split()
consider_numbers = len(numbers_split)

# Выполняю условия задачи для положительных чисел
positiv_numbers = []
for i in numbers_split:
  if int(i) > 0:
    positiv_numbers.append(i)
count_num_positive = len(positiv_numbers)

# Выполняю условия задачи для отрицательных чисел
negative_numbers = []
for i in numbers_split:
  if int(i) < 0:
    negative_numbers.append(i)
count_num_negative = len(negative_numbers)
file_num2.close()

# Создаю новый файл, где по указанному формату вношу данные, которые получила раннее
file_numbers_new = open('information_num.txt', 'w', encoding='utf-8')
file_numbers_new.writelines(f'''Исходные данные: {numbers}
Количество элементов: {consider_numbers}
Положительные числа: {positiv_numbers}
Количество положительных чисел: {count_num_positive}
Отрицательные числа: {negative_numbers}
Количество отрицательных чисел: {count_num_negative}''')

file_numbers_new.close()