"""
Создайте собственный класс-исключение, который должен проверять содержимое списка
на отсутствие элементов типа строка и булево. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class ExcClass:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except ValueError:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Повторить ввод? д/н')
                if y_or_n == 'Д' or y_or_n == 'д':
                    print(excpt.my_input())
                elif y_or_n == 'Н' or y_or_n == 'н':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


excpt = ExcClass(1)
print(excpt.my_input())