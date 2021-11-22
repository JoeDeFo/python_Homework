import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([1, 12])
np.linalg.lstsq(A, B)

def Q(x, y, z):
  return (x**2 + y**2 + z**2)

x = np.linspace(-1, 20, 301)
plt.plot(x, Q(x, 2 * x - 5, 3 * x - 1))
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()