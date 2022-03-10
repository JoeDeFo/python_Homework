"""
В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
получены опытные данные:
6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
оценить истинное значение величины X при помощи доверительного интервала, покрывающего это
значение с доверительной вероятностью 0,95.
"""
import math
import numpy as np
from math import factorial

#Дано
the_value_of_salaries = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
n = 10
t(a/2)(по табличному значению) = 1.96

#Найдем среднюю выборочную и дисперсию

1."""Средняя выборочная""" = 6.59
the_value_of_salaries_arithmetic_mean = the_value_of_salaries.sum() / the_value_of_salaries.size
2."""Дисперсия""" = 0.2032
the_value_of_salaries_dispersion = np.sum((the_value_of_salaries - the_value_of_salaries_arithmetic_mean)**2) / (the_value_of_salaries.size - 1)
#Найдем критерий Стьюдента
t1 = the_value_of_salaries_arithmetic_mean - (t(a/2) * math.sqrt(the_value_of_salaries_dispersion / 10)) = 6.3107
t2 = the_value_of_salaries_arithmetic_mean + (t(a/2) * math.sqrt(the_value_of_salaries_dispersion / 10)) = 6.8693
Ответ: [6.3107,6.8693]