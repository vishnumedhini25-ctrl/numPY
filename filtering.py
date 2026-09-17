import numpy as np

marks = np.array([50,48,90,75,86])

passMarks=(marks[marks>50])
print(passMarks)

passMarks=(marks[marks==50])
print(passMarks)

even=(marks[marks%2==0])
print(even)

even=marks[(marks>=50) & (marks<=80)]
print(even)

even=marks[(marks>50) | (marks%2==0)]
print(even)
 
print(marks)

# filtering in multidimensional array
arr = np.array([[1, 2, 3],
                [4,5,6]])

Even = arr[arr%2==0]
print(Even)

Even = np.where(arr%2==0,arr,0)
print(Even)