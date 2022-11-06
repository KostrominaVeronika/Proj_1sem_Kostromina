# Найти сумму ряда 1...60

def summa(): # функция для нахождения суммы числового ряда
  data = 0
  i = 0
  while i != 61:
      data += i
      i += 1
  return data

try:
    print('Сумма числового ряда =', summa()) # Вызов функции
except TypeError:
    print('Не вводи аргументы!')