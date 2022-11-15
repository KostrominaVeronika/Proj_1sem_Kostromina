import random
list_ = []
for i in range(int(input("Введите кол-во элементов списка: "))):  # Заполнение списка рандомными значениями
  list_.append(random.randint(0, 100))
print(list_)  # вывод списка
print("Измененный вид списка: ",list_[1::2] + list_[::2])  # вывод измененного списка

