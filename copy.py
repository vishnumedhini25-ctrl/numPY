import numpy as np

a = np.array([10, 20, 30, 40])

b = a.copy()

b[0] = 100

print("Original:", a)
print("Copy:", b)

# view
c = a.view()
c[0] = 100
print("Original:", a)
print("View:", c)

# to check view and copy
b=a.copy()
c=a.view()

print(b.base)
print(c.base)