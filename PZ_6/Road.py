class Road:
    _length = 0
    _width = 0

    def asphalt(self):
        return self._length * self._width * 24.6 * 10  # СНиП 4.02-91


road = Road()  # Что-то я ничего не понял про передачу атрибутов при создании экземпляра класса в условии задачи
road._length = 800  # Наверное после определения экземпляра
road._width = 6
print(f'{road.asphalt() / 1000} Тонн')
