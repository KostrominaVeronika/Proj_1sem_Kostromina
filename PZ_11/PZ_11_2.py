# Задача 2
'''Из предложенного текстового файла (text18-13.txt) вывести на экран его содержимое,
количество символов в тексте. Сформировать новый файл, в который поместить текст в
стихотворной форме предварительно вставив после строки N (N – задается пользователем)
произвольную фразу.'''

# Открываю файл с предварительно имеющимся текстом
file_text = open('text18-13.txt', 'r', encoding='utf-8')
file_read = file_text.read()
file_readlines = file_read.split('\n')
file_text.close()
# Выполняю первое условие задачи
print('Содержимое: ', file_read, '\n\nКолличество символов: ', len(file_read), '\n')

try: # Обработка на ввод не целочисленного значения
  n = int(input('Введите номер строки: '))
  word = input('Введите выражение: ')
except ValueError:
  print('Вы ввели не целочисленный тип данных')

# Форматирую по условию текст
new_text = ''
for i, words in enumerate(file_readlines):
  if i == n:
    new_text += word + '\n'
  new_text += words + '\n'

# Создаю новый файл и записываю в него форматированный по условию текс
file_new_text = open('new_text_18_13.txt', 'w', encoding='utf-8')
file_new_text.writelines(new_text)
file_new_text.close()