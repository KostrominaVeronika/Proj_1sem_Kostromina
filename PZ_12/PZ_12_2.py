'''Составить список, в который будут включены только согласные буквы и привести их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели',
'Каир'].'''
old_list_cities = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
new_list_cities = []

# Удаление гласных и преобразовние в высокий регистр
for i in old_list_cities:
    new_list = [j for j in i.lower() if j in 'бвгджзйклмнпрстфхцчшщ']
    new_list_cities.append(''.join(new_list).upper())
print('Список до: ', old_list_cities, 'Список после: ', new_list_cities)
