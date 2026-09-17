import numpy as np
import os

arr = np.array([1,2,3,4,5])
np.save("Data.npy",arr)

read = np.load("Data.npy")
print(read)

Arr = np.array([9,10,11,112,13])
np.savez("data.npz",arr,Arr)

read = np.load("data.npz")
print(read)

print(read["arr_1"])

# Linear Algebra
A = np.array([[1,2],
                [3,4]])
B = np.array([[5,6],
                [7,8]])
print(np.matmul(A,B))
print(B.T)

a=np.array([1,2,3])
b=np.array([4,5,6])

print(np.dot(a,b))
print(np.linalg.det(A))