%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2*np.pi, 3*np.pi, 300)

k, a, b = np.linspace(34, 12, num = 3)
k1, a1, b1 = np.linspace(14, 35, num = 3)
k2, a2, b2 = np.linspace(12, 65, num = 3)


plt.figure(figsize = (5, 5))
plt.plot(x, k * np.cos(x - a) + b)
plt.plot(x, k1 * np.cos(x - a1) + b1, color='yellow')
plt.plot(x, k2 * np.cos(x - a2) + b2, color='green')

plt.xlabel('x')
plt.ylabel('y')
plt.show()