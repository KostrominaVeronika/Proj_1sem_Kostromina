def ShiftRight3(A,B,C):
    A,B = B,A # Смещение А в В
    A,C = C,A # Смещение С в А
    L = [] # пустой список
    L.append(A) # заполнение списка элементами
    L.append(B)
    L.append(C)
    return L # Заполнение списка


print(ShiftRight3(22,32,33)) # Вывод функции с значениями
