# программа расчитывает А**N
try:  # обработчик исключенеий
    a = float(input('Введите число A: '))
    n = int(input('Введите число N: '))
    i = a
    while n > 1:
        a *= i
        n -= 1
    print(a)
except ValueError:
    print("Вы ввели не число, попробуйте снова)")
