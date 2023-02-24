''' В строках исходного текстового файла (dates1.txt) все даты представить в виде
подстроки. Поместить в новый текстовый файл все даты февраля в формате
ДД/ММ/ГГГГ'''
import re

file_dates = open(file='dates1.txt', mode='r', encoding='utf-8')
text = file_dates.read()
file_dates.close()

new_dates_file = ''

for i in re.findall(r'[0-9]{2}\.02\.[0-9]{4}', text):
    new_dates_file += i.replace('.', '/') + '\n'

new_file = open(file='up_dates1.txt', mode='w', encoding='utf-8')
new_file.writelines(new_dates_file)
new_file.close()