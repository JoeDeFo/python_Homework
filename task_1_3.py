"""Окружность"""
% matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

x = []
x2 = []
y = []
y2 = []

for i in range(2000):
    r = 1500
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(r ** 2 - i ** 2))
    y2.append(-np.sqrt(r ** 2 - i ** 2))

plt.figure(figsize=(9, 9))
plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x2, y2)
plt.plot(x2, y)
plt.show()

"""Эллипс"""
% matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math
x = []
x2 = []
y = []
y2 = []

for i in range(2000):
    a = 32
    b = 44
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))

plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x2, y2)
plt.plot(x2, y)
plt.show()

"""Гипербола"""
% matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math
x = []
x2 = []
y = []
y2 = []

for i in range(2000):
    a = 500
    b = 600
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))

plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x2, y2)
plt.plot(x2, y)
plt.show()