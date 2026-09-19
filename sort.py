import numpy as np

a = np.array([40, 10, 50, 20, 30])

print(np.sort(a))
print(np.sort(a)[::-1])

print(np.argsort(a))

# 2D array sorting
a = np.array([[30, 10, 20],
              [60, 40, 50]])

print(np.sort(a))

# column wise sorting
a = np.array([[60, 10, 20],
              [30, 40, 50]])

print(np.sort(a, axis=0))

# row wise sorting
a = np.array([[30, 10, 20],
              [60, 40, 50]])

print(np.sort(a, axis=1))