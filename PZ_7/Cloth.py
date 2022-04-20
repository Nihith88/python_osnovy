"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов
на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу
декоратора @property.
"""

from abc import ABC, abstractmethod


class AbstractClothes(ABC):  # Абстрактный класс для всех предметов одежды

    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name, measuring):
        self.name = name
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self):
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self):
        return self._measuring

    @measuring.setter
    def measuring(self, measuring):
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        return f"Всего {sum([item.tissue_required for item in self._clothes])} кв.м для пошива"


class Coat(Clothes):
    # класс пальто дочерний от одежды
    def _calc_tissue_required(self):
        #  расход ткани для пальто
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self):
        return self.measuring

    @V.setter
    def V(self, size):
        self.measuring = size

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера требуется {self.tissue_required} кв. м ткани"


class Suit(Clothes):  # костюм - дочернй класс от одежды

    def _calc_tissue_required(self):
        """ посчитать расход ткани для костюма """
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self):
        return self.measuring

    @H.setter
    def H(self, height):
        self.measuring = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. требуется {self.tissue_required} кв. метров ткани"


coat = Coat('Пальто', 42)
print(coat)
suit = Suit('Костюм', 150)
print(suit)
print(suit.total_tissue_required)

suit.H = 185  # установка нового размера
print(suit)
coat.V = 56  # установка нового размера
print(coat)
print(suit.total_tissue_required)
