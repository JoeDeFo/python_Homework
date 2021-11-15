%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

"""
Напишите код, проверяющий любую из теорем сложения или умножения вероятности на 
примере рулетки или подбрасывания монетки.
"""
x,y,z = 0, 0, 0
for i in range(50):
    a = np.random.uniform(0, 10)
    z = z + 1
    if a < 5 :
        x = x + 1
    else:
        y = y + 1
if x + y == z:
  print('True')
else:
  print('False')

"""
Сгенерируйте десять выборок случайных чисел х0, …, х9.
и постройте гистограмму распределения случайной суммы  +х0+ …+ х 9. 
"""

sums = []
for i in range(100):
  x = np.random.randn(10)
  sums.append(sum(x))
  i += 1
num_bins = 10
n, bins, patches = plt.hist(sums, num_bins)
plt.xlabel('sum')
plt.ylabel('Probability')
plt.title('Histogram')