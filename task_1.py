"""
Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).
"""

%matplotlib inline
import numpy as np

for i in range(10):
    a = input()
    x = int(np.random.uniform(0,36))
    if x == 0:
        print('dropped out zero')
    elif x % 2 == 0:
        print(f'dropped a black cell numbered - {x}')
    elif x % 1 == 0:
        print(f'dropped a red cell numbered - {x}')

