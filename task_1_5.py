"""Нарисуйте трехмерный график двух параллельных плоскостей."""
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
my_figure = figure(figsize = (16, 16))
my_axes = Axes3D(my_figure)
X = np.arange(-30, 30, 5)
Y = np.arange(-30, 30, 5)

X, Y = np.meshgrid(X, Y)
Z = 9*X + 35
Z2 = 9*X + 200
my_axes.plot_wireframe(X, Y, Z, colors='red')
my_axes.plot_wireframe(X, Y, Z2, colors='yellow')

"""Нарисуйте трехмерный график двух любых поверхностей второго порядка."""
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
my_figure = figure(figsize = (10, 10))
my_axes = Axes3D(my_figure)
a = 45
b = 100

X, Y = np.meshgrid((np.arange(-30, 30, 5)), (np.arange(-30, 30, 5)))

Z = b ** 2 + (b ** 2 * (X ** 2 / a ** 2))
Z1 = -(b ** 2 + (b ** 2 * (X ** 2 / a ** 2)))
Z2 = 2*a*X ** np.cos(40) + np.sqrt(2*a*X ** np.cos(40))
my_axes.plot_surface(X, Y, Z, color='red')
my_axes.plot_surface(X, Y, Z1, color='yellow')

u = np.linspace(0,2*np.pi, 28)
v = np.linspace(0, np.pi, 14)

x = 8 * np.outer(np.cos(u), np.sin(v))
y = 60 * np.outer(np.sin(u), np.sin(v))
z = -400 * np.outer(np.ones(np.size(u)), np.cos(v))

my_axes.plot_surface(x, y, z, color='green')