"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""

class DivisionZ:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def div_null(divider, denominator):
        try:
            return (divider / denominator)
        except ZeroDivisionError:
            return (f"Деление на ноль недопустимо")


div = DivisionZ(10, 100)
print(DivisionZ.div_null(5, 0))
print(DivisionZ.div_null(50, 10))
print(div.div_null(100, 0))