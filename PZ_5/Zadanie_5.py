"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран
"""
import random


numbers = []
for i in range(1, random.randint(50, 500)):
    numbers.append(str(round((random.uniform(1, 2**16)), 3)))
with open('file_5.txt', 'w') as file_5:  # Откроем файл и запишем в него строку чисел
    file_5.write(' '.join(numbers))

with open('file_5.txt', 'r') as file_5:  # Прочитаем содержимое файла
    for line in file_5:
        read_numbers = line.split()
print(f"Сумма чисел в файле: {sum(map(float, read_numbers))}")
