"""
Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    title = None

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print("Начало ввдоа рукописного текста")


class Pencil(Stationery):
    def draw(self):
        print("Начало построения чертежа")


class Handle(Stationery):
    def draw(self):
        print("Начало рисования на доске")


bic = Pen()
kohinoor = Pencil()
erichkrause = Handle()

bic.draw()
kohinoor.draw()
erichkrause.draw()
