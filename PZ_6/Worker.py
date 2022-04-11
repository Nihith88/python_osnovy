"""
Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""


class Worker():
    name = None
    surname = None
    position = None
    _income = {'wage': 0.00, 'bonus': 0.00}


class Position(Worker):
    def __init__(self):
        self.typoname = input('Type employee name: ')
        self.income = int(input('type total income: '))

    def get_full_name(self):
        self.fullname = self.typoname.split()
        Worker.name = self.fullname[0]
        Worker.surname = self.fullname[1]


    def get_total_income(self):
        Worker._income['wage'] = self.income - (self.income / 5)
        Worker._income['bonus'] = self.income / 5


pos1 = Position()
pos1.get_full_name()
pos1.get_total_income()
pos1.position = 'Security'
print(f" Имя: {pos1.name}, фамилия: {pos1.surname}, должность: {pos1.position}, доход: {pos1._income}")

pos2 = Position()
pos2.get_full_name()
pos2.get_total_income()
pos2.position = 'Operator'
print(f" Имя: {pos2.name}, фамилия: {pos2.surname}, должность: {pos2.position}, доход: {pos2._income}")

