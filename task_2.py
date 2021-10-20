"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def TissueConsumption(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def TissueConsumption(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def TissueConsumption(self):
        return 2 * self.h + 0.3

    def SumTissueConsumption(self, list_costumes):
        i = 0
        for item in list_costumes:
            i += item.TissueConsumption
            return i


coat = Coat(63)
costume = Costume(1.56)
costume_1 = Costume(1.45)
costume_2 = Costume(1.78)
costume_3 = Costume(1.94)
list_TissueConsumption = [costume_1, costume_2, costume_3, costume]
print(coat.TissueConsumption)
print(costume.TissueConsumption)
print(costume.SumTissueConsumption(list_TissueConsumption))



