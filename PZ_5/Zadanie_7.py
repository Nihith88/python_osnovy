"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json
from typing import Dict

firms_dict: Dict[str, float] = {}
profit_list = []

with open('firms.txt', mode='r', encoding='UTF-8') as firms:
    for line in firms:  # Чтение строк из файла
        firm_list = line.split()  # Создание списка для каждой фирмы
        firms_dict[firm_list[0]] = float(firm_list[2]) - float(firm_list[3])  # Заполнение словаря ключем
    profit_dict = firms_dict.copy()  # Промежуточный словарь для прибыльных фирм
    for key in firms_dict.keys():
        if firms_dict[key] < 0:
            profit_dict.pop(key)

    profit = sum(profit_dict.values()) / len(profit_dict)
    profit_list.append(firms_dict)  # Если фирма получила убытки, также добавить её в словарь (со значением убытков)
    profit_list.append({'Средняя прибыль': profit})

    with open('result.json', mode='w', encoding='UTF-8') as result:
        json.dump(profit_list, result)
