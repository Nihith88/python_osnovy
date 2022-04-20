import time
import colorama


class TrafficLight:
    __color = None

    def timer(self, __limit):  # Генератор секунд работы светофора
        for sec in range(__limit):
            time.sleep(1)
            print(f" Time remaining: {__limit - sec}")

    def running(self):
        TrafficLight.__color = "red"
        print(colorama.Fore.RED, colorama.Style.BRIGHT, TrafficLight.__color)
        TrafficLight.timer(self, 7)
        TrafficLight.__color = "yellow"
        print(colorama.Fore.YELLOW, colorama.Style.BRIGHT, TrafficLight.__color)
        TrafficLight.timer(self, 2)
        TrafficLight.__color = "green"
        print(colorama.Fore.LIGHTGREEN_EX, colorama.Style.BRIGHT, TrafficLight.__color)
        TrafficLight.timer(self, 7)

    @property
    def color(self):
        return self.__color


mc = TrafficLight()

while True:
    mc.running()
    if mc.color != 'green':
        break
