while True:
    try:  # Определяет тип введенных данных, если встречает текст, выдает ошибку.
        year = int(input("Введите номер года "))
        if (year % 4 == 0 or year % 400 == 0) and (year % 100 != 0):  # Определяет високосный год или нет.
            print("Високосный - 366 дней")
            break
        else:
            print("Невисокосный - 365 дней")
            break
    except ValueError:
        print("Произошла ошибка, введен не верный тип данных!")
        double_var = input('\nХотите попробовать снова? (да или Enter | нет): ')
        if double_var.lower() in ['', 'да']:  # Условие для повторного ввода и обработки данных.
            continue
        else:
            print('Пока!')
            break
