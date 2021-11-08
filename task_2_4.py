"""
y = x2 – 1
exp(x) + x(1 – y) = 1
"""
y = x2 – 1
y = (exp(x) + x –  1) / x

%matplotlib inline
import matplotlib.pyplot as plt
import math
import numpy as np

x = np.linspace(-4, 6, 201)

plt.plot(x, (np.exp(x) + x - 1) / x)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1,5)
plt.grid(True)
plt.show()

from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return (x ** 2 - 1 - y, np.exp(x) + x * (1 - y) - 1)

x1, y1 = fsolve(equations, (1, 1))

print(x1, y1)

"""
y = x2 – 1
exp(x) + x∙(1 – y)  - 1 > 0
"""
y = x2 – 1
y = -1/x +2

%matplotlib inline
import matplotlib.pyplot as plt
import math
import numpy as np

x = np.linspace(-4, 6, 201)

plt.plot(x, (- 1 / x) + 2)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1,5)
plt.grid(True)
plt.show()

from scipy.optimize import fsolve


def equations(p):
    x, y = p
    return (x ** 2 - 1 - y, (- 1 / x) + 2 - y)


x1, y1 = fsolve(equations, (1, 1))

print(x1, y1)

