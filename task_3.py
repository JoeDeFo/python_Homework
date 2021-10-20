"""
Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
"""

class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)
    def __sub__(self, other):
        sub = self.number - other.number
        if sub >= 0:
            return Cell(sub)
        else:
            print(f"Ошибка")

    def __mul__(self, other):

        return Cell(int(self.number * other.number))

    def __truediv__(self, other):

        return Cell(round(self.number // other.number))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(self.number // cells_in_row):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.number % cells_in_row)} \n'
        return row

cell_1 = Cell(17)
cell_2 = Cell(32)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(3))
print(cell_2.make_order(11))
