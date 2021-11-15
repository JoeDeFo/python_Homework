import numpy as np
import math
from pylab import *
import numpy as np
import itertools

k,n = 0, 4
x = np.random.randint(0, 2, n)
y = np.random.randint(0, 2, n)
z = np.random.randint(0, 2, n)
q = np.random.randint(0, 2, n)
a = x + y + z + q
for i in range(0,n):
    if a[i] == 2:
        k = k + 1
result_1 = math.factorial(k) * math.factorial(n - k)
result_2 = math.factorial(n) / result_1
result = result_2 / 2 ** n
print(result)
print(k, n, k/n)



"""
Повторите расчеты биномиальных коэффициентов и вероятностей k успехов 
в последовательности из n независимых испытаний, взяв другие значения n и k.
"""

k, n = 6, 10
result_1 = math.factorial(k) * math.factorial (n - k)
result_2 = math.factorial(n) / result
result = result_2 / 2 ** n
print(result)
print(k, n, k/n)