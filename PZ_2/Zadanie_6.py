"""
6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками
товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно, запросив все данные
у пользователя.
"""
number = 1
goods = []
numeric_goods = []
goods_dict = {"название": None, "цена": None, "количество": None, "ед. изм": None}
while True:
    goods_dict["название"] = input("Введите название " + str(number) + " товара: ")
    goods_dict["цена"] = float(input("Введите цену " + str(number) + " товара: "))
    goods_dict["количество"] = float(input("Введите кол-во " + str(number) + " товара: "))
    goods_dict["ед. изм"] = input("Введите ед. изм " + str(number) + " товара: ")
    buffer = goods_dict.copy()  # необходимо сделать копию словаря, т.к. это изм. тип данных и в памяти это один объект
    goods.append((number, buffer))
    number += 1
    choice = input("Продолжить ввод товаров? (1 - да, 0 - нет):  ")
    if choice == '0':
        break

# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например,
# название. Тогда значение — список значений-характеристик, например, список названий товаров.

analytic_names = []
analytic_prices = []
analytic_qty = []
analytic_units = []
for i in range(0, len(goods)):  # проходим по порядку элементов нашего списка
    buffer_1 = goods[i]  # и "распаковываем наши данные из элементов
    buffer_2 = buffer_1[1]
    buffer_3 = list(buffer_2.values())
    analytic_names.append(buffer_3[0])  # собираем наши списки аналитики по параметрам товаров
    analytic_prices.append(buffer_3[1])
    analytic_qty.append(buffer_3[2])
    analytic_units.append(buffer_3[3])
analytic_goods = {"название": analytic_names, "цена": analytic_prices, "количество": analytic_qty,
                  "ед.изм.": list(set(analytic_units))}  # собираем аналитический объект - словарь
print(analytic_goods)