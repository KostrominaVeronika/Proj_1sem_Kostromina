import random
n = random.randrange(2, 10)
a = [random.randrange(1,10) for i in range(n)]  # Заполнение списка рандомными значениями
r = random.randrange(2, 10)
print("Список:", a)
print("R:",r)
d_m = abs(r - (a[0] + a[1]))  # Модуль для минимального обозначения сумма элементов
i_m = 1
for i in range(n):  # Цикл с высчитыванием суммы близкой к числу r и нахождение этих элементов в цикле
    d_t = abs(r - (a[i-1] + a[i]))
    if d_m > d_t :
        d_m = d_t
        i_m = i
if a.index(a[i_m-1]) < a.index(a[i_m]):  # Вывод двух элементов в порядке возрастания индексов
  print(a[i_m-1], a[i_m])
else:
  print(a[i_m], a[i_m-1])