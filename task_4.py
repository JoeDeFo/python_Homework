"""
Продавец утверждает, что средний вес пачки печенья составляет 200 г.
Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально.
Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?
"""

import math
import numpy as np
from math import factorial

#Дано
the_value_of_salaries = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
n = 10
t(a/2)(по табличному значению) = 1.96


#Найдем среднюю выборочную и дисперсию

1."""Средняя выборочная""" = 198.5
the_value_of_salaries_arithmetic_mean = the_value_of_salaries.sum() / the_value_of_salaries.size
2."""Дисперсия""" = 19.833
the_value_of_salaries_dispersion = np.sum((the_value_of_salaries - the_value_of_salaries_arithmetic_mean)**2) / (the_value_of_salaries.size - 1)
#Найдем критерий Стьюдента
t1 = the_value_of_salaries_arithmetic_mean - (t(a/2) * math.sqrt(the_value_of_salaries_dispersion / 10)) = 193.924
t2 = the_value_of_salaries_arithmetic_mean + (t(a/2) * math.sqrt(the_value_of_salaries_dispersion / 10)) = 203.076