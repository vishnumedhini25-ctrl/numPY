import numpy as np

# 2D array
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(array.ndim)
print(array[1][1])

# 3D array
arr=np.array([[[1,2,3],[4,5,6]],
              [[11,22,33],[7,8,9]]])
print(arr)
print(arr.ndim)
print(arr[1][0][2])

print(arr[1,0,2])

print(arr.shape)

num = np.array([1,2,3,4,5,6,7,8,9,10])
print(num.shape)
num=num.reshape(2,5)
print(num)

arr=arr.reshape(2,6)
print(arr)

arr=arr.reshape(-1,3)
print(arr)
