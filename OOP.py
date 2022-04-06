class Auto:  # Описание имени класса
    # Атрибуты класса
    auto_vendor = "Toyota"
    auto_model = "Camry 55"
    auto_hp = 277
    auto_year = 2013

    # Методы класса
    def on_auto(self):
        print("Engine start")

    def off_auto(self):
        print("Engine stop")


a = Auto()  # Создание экземпляра класса
print(a.auto_vendor)
print(a.auto_model)
print(a.auto_hp)
print(a.auto_year)
a.on_auto()
a.off_auto()  # теперь можем обращаться ко всем атрибутам и методам родительского класса


class Car:
    car_count = 0  # Атрибут класса

    def car_start(self, car_name, car_model, car_year):  # Метод класса
        print("Engine is started")
        self.car_name = car_name
        self.car_model = car_model
        self.car_year = car_year
        Car.car_count += 1


car = Car()
car.car_start("Lexus", "RX 350", 2020)
print(car.car_name)
print(car.car_year)

car_2 = Car()
car_2.car_start("Lada", "Granta", 2018)
print(car.car_name)
print(car.car_year)


class Bike:
    auto_count = 0

    def __init__(self):  # Конструктором в ООП называется специальный метод, вызываемый при создании экземпляра класса.
        # Этот метод определяется с помощью конструкции __init__.
        Bike.auto_count += 1
        print(Bike.auto_count)


b1 = Bike()
b2 = Bike()
b3 = Bike()
"""Для каждого экземпляра значение атрибута
auto_count возрастает и выводится на экран. На практике конструкторы используются для
инициализации значений атрибутов. Это важно при создании объекта класса"""

class Myclass:
    _attrib = "my personal attrib"
    def method(self):
        print("It is protected method")

class Transport:
    def trans_method(self):
        print('parent method')

class Vehicle(Transport):
    def veh_method(self):
        print('legacy method')

vm = Vehicle()
vm.trans_method()

class Shape:
    def __init__(self, color, param1, param2):
        self.color = color
        self.param1 = param1
        self.param2 = param2

    def sqare(self):
        return self.param1 * self.param2

class Rectangle(Shape):
    def __init__(self, color, param1, param2, rect_p):
        super().__init__(color, param1, param2)
        self.rect_p = rect_p

    def get_r_p(self):
        return self.rect_p

class Triangle(Shape):
    def __init__(self, color, param1, param_2, triangle_p):
        super().__init__(color, param1, param_2)
        self.triangle_p = triangle_p

    def get_t_p(self):
        return self.triangle_p

r = Rectangle('white', 100, 200, True)
print(r.color)
print(r.sqare())
print(r.get_r_p())
t = Triangle('red', 30, 21, False)
print(t.color)
print(t.sqare())
print(t.get_t_p())

