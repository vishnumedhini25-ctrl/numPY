import numpy as np

number = np.array([10, 20, 30, 40])

print(number)

print(number * 2)

Number = np.array([5,6,7,9])
print(number + Number)

print (number.ndim)
print (number.dtype) 
print (number.nbytes)

number = np.array([10, 20, 30, 40],dtype=np.int8)
print (number.nbytes)

number = np.array([10, 20, 30, 40],dtype=np.int16)
print (number.nbytes)

number = np.array([100, 550, 830, 400],dtype=np.int32)
print(f"{number.nbytes} bytes")

Array = np.array([1.2,2.1,3.0,5.9])
print(Array)
print(Array.dtype)
print(Array.nbytes,"bytes")

Array = np.array([1.2,2.1,3.0,5.9],dtype=np.float16)
print(Array.dtype)
print(Array.nbytes,"bytes")

number = np.array([10, 20, 30, 40],dtype=np.float16)
print(number)
print(number.dtype)
print (number.nbytes,"bytes")

arr = np.array([True, False, True, False])
print(arr)
print(arr.dtype)
print(arr.nbytes,"bytes")

number = np.array([10, 20, 30, 40],dtype=np.str_)
print(number)
print(number.dtype)
print (number.nbytes,"bytes")


number = np.array([10, 20, 30, 40])
number=number.astype(np.str_)

print(number)
print(number.dtype) 
print (number.nbytes,"bytes")