# Программа рассчитывает сумму последовательности 1 + 2 + ... + N

try:  # Обработчик исключений
    n = int(input('Введите число N: '))
    if n > 1:  # Условие на проверку N > 1
        k = 1
        summa = 0
        while summa < n:  # Цикл, в котором рассчитывается сумма 1 + 2 + ... + N
            k += 1
            summa += k
        print('Сумма =', summa, '\nЧисло K =', k)
    else:
        print('Число N >= 0 !')
except ValueError:
    print('Введен неверный тип данных! Введите число!')
