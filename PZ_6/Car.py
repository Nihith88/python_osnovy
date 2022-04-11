"""
Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
© geekbrains.ru 19
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
"""


class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def go(self):
        print(f"{self.color} {self.name} начала движение")

    def stop(self):
        print(f"{self.color} {self.name} остановилась")

    def turn(self, direction):
        print(f"{self.color} {self.name} повернула в{direction}")

    def show_speed(self, speed):
        print(f"Текущая скорость {self.name}: {speed} км/ч")


class TownCar(Car):
    def show_speed(self, speed):
        print(f"Текущая скорость {self.name}: {speed} км/ч")
        if self.speed > 60:
            print("!Превышение скорости!")



class WorkCar(Car):
    def show_speed(self, speed):
        print(f"Текущая скорость {self.name}: {speed} км/ч")
        if speed > 40:
            print("!Превышение скорости!")



class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


kia = TownCar()
kia.name = 'Cerato'
kia.color = 'silver'
kia.speed = 65

truck = WorkCar()
truck.name = 'MAN'
truck.color = 'orange'
truck.speed = 45

toyota = SportCar()
toyota.name = 'Supra'
toyota.color = 'Black'
toyota.speed = 120

bobik = PoliceCar()
bobik.name = 'UAZ-469'
bobik.color = 'white with blue strip'
bobik.speed = 3 * 10**8

kia.go()
kia.show_speed(kia.speed)
kia.turn('право')
kia.stop()

truck.go()
truck.show_speed(truck.speed)
truck.turn('лево')
truck.stop()

toyota.go()
toyota.show_speed(toyota.speed)
toyota.turn('право')
toyota.stop()

bobik.go()
bobik.show_speed(bobik.speed)
bobik.turn('hyperloop')
bobik.stop()


