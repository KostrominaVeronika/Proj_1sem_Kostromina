# Подсчет цифр с строке

try:  # Обработчик ошибок
    s = input('Введите значение: ')
    k = 0
    for i in s:
        if i.isdigit():  # Проверка символа на то, что это цифра с помощью метода
            k += 1
    print('Цифр в вашем выражении: ', k)
except ValueError:
    print('Выражение содержит неправильные символы!')
