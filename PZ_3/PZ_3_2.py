# Программа для определения високосного года

try:  # Обработчик ошибок
    year = int(input("Введите год"))
    if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):  # Условие на проверку високоный ли год
        print(" Год високосный, 366 дней ")
    else:
        print("Год невисокосный, 365 дней")
except ValueError:
    print("Введен неверный тип данных!")
