# In NumPy, broadcasting is a concept that lets you perform operations on arrays of different shapes without manually resizing them. 

# Two dimensions are compatible if:
# They are equal
# OR one of them is 1


import numpy as np 
array1=np.array([1,2,3])
array2=np.array([[1],[2],[3]])

print(array1+array2)