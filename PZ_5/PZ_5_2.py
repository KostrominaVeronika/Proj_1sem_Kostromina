# Описать функцию выполняющую правый циклический сдвиг

def ShiftRight3(A,B,C):  # создание функции для правого сдвига
    A, B = B, A  # Смещение А в В
    C, A = A, C  # Смещение С в А
    return A, B, C

try:  #
  A, B, C = 2, 3, 4
  print('Было A = '+str(A), 'B = '+str(B), 'C = '+str(C))
  A, B, C = ShiftRight3(A, B, C) # вызов функции с перыми входными данными
  print('Стало A = '+str(A), 'B = '+str(B), 'C = '+str(C))
  print('\nВторой заход')
  A, B, C = 8, 4, 7
  print('Было A = '+str(A), 'B = '+str(B), 'C = '+str(C))
  A, B, C = ShiftRight3(A, B, C) # вызов функции со вторыми входными данными
  print('Стало A = '+str(A), 'B = '+str(B), 'C = '+str(C))
except TypeError:
  print('Неверный аргумент')
