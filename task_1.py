"""
Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75,
65, 84, 90, 150. Посчитать (желательно без использования статистических методов наподобие std, var, mean)
среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
"""
import numpy as np
from math import factorial

the_value_of_salaries = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

1."""Cреднее арифметическое"""
the_value_of_salaries_arithmetic_mean = the_value_of_salaries.sum() / the_value_of_salaries.size
2."""Cреднее квадратичное отклонение"""
the_value_of_salaries_standard_deviation = (np.sum((the_value_of_salaries - the_value_of_salaries_arithmetic_mean)**2) / the_value_of_salaries.size)**0.5
3."""Cмещенная дисперсия"""
the_value_of_salaries_shifted_variance = np.sum((the_value_of_salaries - the_value_of_salaries_arithmetic_mean)**2) / the_value_of_salaries.size
4."""Несмещенная дисперсия"""
the_value_of_salaries_unbiased_variance = np.sum((the_value_of_salaries - the_value_of_salaries_arithmetic_mean)**2) / (the_value_of_salaries.size - 1)
