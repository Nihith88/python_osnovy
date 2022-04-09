"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""
word_count = {}
string_count = 0
with open('user_2.txt', mode='r', encoding='UTF-8') as usr_file:
    for line in enumerate(usr_file):
        word_count[line[0]] = len(line[1].split())
        string_count += 1
print(f"В файле {usr_file.name} количество строк: {string_count}")
for i in word_count.keys():
    print(f"Строка {i}: слов - {word_count[i]}")

