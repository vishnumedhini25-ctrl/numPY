import numpy as np

arr1 = np.zeros((4,2))
print(arr1)

arr2 = np.ones((3,4))
print(arr2)

arr3 = np.full(2,4)
print(arr3)

arr4 = np.full((2,3),45)
print(arr4)

arr5 = np.eye(5)
print(arr5)

arr6 =np.arange(0,100,2)
print(arr6)

arr7 = np.linspace(0,100,5)
print(arr7)

print(np.sum(arr6))

print(np.min(arr6))
print(np.max(arr6))
print(np.median(arr6))
print(np.std(arr6))

arr8 = np.array([[1,2,3],
                 [4,5,6]])
print(np.sum(arr8))
print(np.sum(arr8,axis=0))
print(np.sum(arr8,axis=1))