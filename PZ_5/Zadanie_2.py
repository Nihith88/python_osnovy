"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""

string_count = 0
with open('user_2.txt', 'r') as usr_file:
    for line in usr_file:
        string_count += 1
print(f"В файле {usr_file.name} количество строк: {string_count}")

