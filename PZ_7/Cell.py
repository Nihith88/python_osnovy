"""
Реализовать программу работы с органическими клетками, состоящими
из ячеек. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству ячеек клетки
(целое число). """


class Cell:
    def __init__(self, count):
        self._count = count

    # Например, количество ячеек клетки равняется 12, количество ячеек
    # в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
    # Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
    # Тогда метод make_order() вернет строку: *****\n*****\n*****.

    # Сложение. Объединение двух клеток. При этом число ячеек общей
    # клетки должно равняться сумме ячеек исходных двух клеток.
    def __add__(self, o: "Cell") -> "Cell":
        return Cell(self._count + o._count)

    # Вычитание. Участвуют две клетки. Операцию необходимо выполнять
    # только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

    def __sub__(self, o: "Cell") -> "Cell":  # Перегрузка метода __sub__
        if self._count > o._count:
            return Cell(self._count - o._count)
        print(f"{self._count} - {o._count}: Аннигиляция клетки ¯\_(ツ)_/¯")

    # Умножение. Создается общая клетка из двух. Число ячеек общей
    # клетки определяется как произведение количества ячеек этих двух клеток.

    def __mul__(self, o: "Cell") -> "Cell":
        return Cell(self._count * o._count)

    # Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
    # деление количества ячеек этих двух клеток.

    def __truediv__(self, o: "Cell") -> "Cell":
        return Cell(self._count // o._count)

    # В классе необходимо реализовать метод make_order(), принимающий
    # экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.

    def make_order(self, per_row: int) -> str:
        # Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
        # аргументу. Если ячеек на формирование ряда не хватает, то в последний
        # ряд записываются все оставшиеся.
        rows, tail = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self._count} ячеек"


c1 = Cell(17)
print(c1)
c2 = Cell(5)
print(c2)

print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c2 - c2)
print(c1 * c2)
print(c1 / c2)
print((c1 * c2).make_order(18))
