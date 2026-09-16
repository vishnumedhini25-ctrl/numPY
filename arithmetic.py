import numpy as np

arr = np.array([25,24,5,2])

print(arr+3)

print(arr-5)

print(arr*6)
print(arr ** 5)

print(arr/2)

Square=np.sqrt(arr)
print(Square)

print(np.round(Square))

Arr=np.array([[2,4,6,8]])
print(arr+Arr)
print(arr-Arr)
print(arr*Arr)
print(arr/Arr)

print(np.pi)
print(2*np.pi*Arr)

# Comparison operators
Age=np.array([25,24,53,18,6,17])
print(Age<18)

print(Age==18)

print(Age>=18)

Age[Age<18]=18
print(Age)

Age[Age>50] = 50
print(Age)