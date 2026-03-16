import numpy as np 
array=np.array([[["a","b","c"],
                 ["d","e","f"],
                 ["g","h","n"]]])
print(array.shape)
print(array.ndim)

word=array[0,2,1]+array[0,1,1]+array[0,2,2]
print(word)