"""
6.1. итератор, генерирующий целые числа, начиная с указанного
"""

from sys import argv
import itertools

script_name, start_gen = argv

print(f"Начало работы скрипта. Старт генератора с {start_gen}")
for el in itertools.count(int(start_gen)):
    if el >= 18:
        break
    else:
        print(el)
