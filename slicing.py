import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr)
print(arr[0])
print(arr[-1])

print(arr[1][2])

# Row wise slicing
print(arr[1:3])
print(arr[0:3:1])
print(arr[:2])

print(arr)
print(arr[:-1])

# Column wise slicing
print(arr)
print(arr[:,0:2])
print(arr[:,1:3:2])
print(arr[:3:2,1:3])

print(arr[1:3:1,1:3])
print(arr[1:3,0:2])