"""
Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import datetime


class Date:
    def __init__(self, dd_mm_yyyy):
        self.day_month_year = str(dd_mm_yyyy)

    @classmethod  # Извлекаем число месяц год и переводим в числа
    def extract(cls, dd_mm_yyyy):
        my_date = []

        for i in dd_mm_yyyy.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod  # Валидатор
    def valid(day, month, year):
        try:
            if datetime.datetime(year=year, month=month, day=day):
                return f"Дата корректная"
        except ValueError:
            return f"Неверный ввод"

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


today = Date('20 - 4 - 2022')
print(today)
print(Date.valid(31, 11, 2022))
print(today.valid(11, 13, 2011))
print(Date.extract('10 - 11 - 1988'))
print(today.extract('10 - 10 - 2010'))
print(Date.valid(1, 11, 2000))
