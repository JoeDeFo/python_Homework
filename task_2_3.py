"""Напишите код, который будет переводить полярные координаты в декартовы."""
%matplotlib inline
import matplotlib.pyplot as plt
import math
def polar_to_cartesian(a,b):
    x = a*math.cos(b)
    y = a*math.sin(b)
    return x,y

"""Напишите код, который будет рисовать график окружности в полярных координатах."""
%matplotlib inline
import matplotlib.pyplot as plt
import math
import numpy as np
a = np.arange(0., 4., 4./180.)*np.pi
plt.polar(a, [5]*len(a))
plt.show()

"""Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах."""
%matplotlib inline
import matplotlib.pyplot as plt
import math
import numpy as np
a = np.arange(1, 5, 2)
print(a)
b = np.arange(1, 5, 2)
print(b)
plt.polar(a, b)
plt.show()


