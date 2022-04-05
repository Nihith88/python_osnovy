"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
"""

work_dict = {}
with open('staff.txt', mode='r', encoding='UTF-8') as staff:
    for line in staff:
        list_line = line.split()
        work_dict[list_line[0]] = float(list_line[1])

print(f" Сотрудники-'счастливчики': {', '.join([name for name in work_dict.keys() if work_dict[name] < 20000])}.")
print(f" Средняя заработная плата: {round(sum(work_dict.values()) / len(work_dict), 2)} руб.")
