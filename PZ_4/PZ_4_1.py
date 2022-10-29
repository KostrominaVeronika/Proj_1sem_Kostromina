#программа расчитывает А**N
try:# обработчик исключенеий
  a = float(input())
  n = int(input())
  i = a
  while n > 1:
    a *= i
    n -= 1
  print(a)
except:
  print("вы ввели не число, попробуйте снова)")