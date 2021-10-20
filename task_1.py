"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""

class Matrix:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for a in range(len(self.list_1)):

            for b in range(len(self.list_2[a])):
                matrix[a][b] = self.list_1[a][b] + self.list_2[a][b]

        return str('\n'.join(['\t'.join([str(b) for b in a]) for a in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(b) for b in b]) for a in matrix]))

my_matrix = Matrix([[6, 11, 15],
                    [56, 85, 31],
                    [21, 60, 10]],
                   [[54, 34, 80],
                    [10, 1, 3],
                    [45, 63, 31]])
print(my_matrix.__add__())