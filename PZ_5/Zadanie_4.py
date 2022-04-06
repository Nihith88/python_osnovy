"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл
"""

translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('eng.txt', 'r') as eng:
    f_obj = open('ru.txt', mode='w', encoding='UTF-8')
    for line in eng:
        tmp_list = line.split()
        tmp_list[0] = translator[tmp_list[0]]
        f_obj.write(' '.join(tmp_list) + '\n')
    f_obj.close()
