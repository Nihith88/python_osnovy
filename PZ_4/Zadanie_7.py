"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция вызывается
следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле
нужно выводить только первые n чисел, начиная с 1! и до n!.
"""

from math import factorial


def fact(n):
    facts = list(map(lambda x: factorial(x), [i for i in range(1, n + 1)]))
    for elem in facts:
        yield elem


n = int(input("Введите число n:  "))
for el in fact(n):
    print(el)
