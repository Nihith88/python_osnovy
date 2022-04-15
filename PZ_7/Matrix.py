"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы."""


class Matrix:

    def __init__(self, matrix_data):  # Перегрузка конструктора класса
        self.matrix = matrix_data

        qty_el = len(self.matrix)
        for stroka in self.matrix:
            self.matrix_size = tuple([(qty_el, len(stroka))])

        if len(self.matrix_size) != 1:
            raise ValueError("Неверный размер матрицы (╮°-°)╮┳━━┳ ( ╯°□°)╯ ┻━━┻")

# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

    def __str__(self) -> str:  # Перегрузка метода __str__
        return '\n'.join(['\t'.join(map(str, elem)) for elem in self.matrix])

# реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица

    def __add__(self, o: "Matrix") -> "Matrix":  # Перегружаем метод __add__
        if not isinstance(o, Matrix):
            raise TypeError(f"'{o.__class__.__name__}' "
                            f"Тип объекта не соответствует")
        if self.matrix_size != o.matrix_size:
            raise ValueError(f"Разные размеры матриц")

        result = []

        for item in zip(self.matrix, o.matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)


matrix1 = Matrix([[1, 3, 5, 7], [2, 4, 6, 8], [10, 10, 10, 10]])
print(matrix1, '\n')

matrix2 = Matrix([[10, 30, 50, 70], [20, 40, 60, 80], [100, 100, 100, 100]])
print(matrix2, '\n')

print(matrix1 + matrix2)

