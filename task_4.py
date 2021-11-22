import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg

A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
P, L, U = scipy.linalg.lu(A)

print(P)
print(L)
print(U)
print(np.dot(P.transpose(), A) - np.dot(L, U))

L = np.array([ [1, 0, 0], [0.25, 1, 0], [0.5, -0.4, 1]])
U = np.array([ [4, 28, 73], [0, -5, -15.25], [0, 0, -21.6]])
A = np.dot(L, U)
P, L, U = scipy.linalg.lu(A)

print("det A = ", np.linalg.det(A))
print("A = ", A)
print("P = ", P)
print("L = ", L)
print("U = ", U)

B = np.array([3, 8, 5])
np.linalg.solve(A, B)