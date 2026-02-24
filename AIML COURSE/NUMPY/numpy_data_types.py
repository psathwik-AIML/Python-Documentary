# d type :
# the data type is used for memory effiecient 


# 1 byte = 8 bits 
import numpy as np
array=np.array([1,2,0,5],dtype=np.bool_)
print(array)
print(f"d type is : {array.dtype}")
print(f"d type is : {array.nbytes}")

array=array.astype(np.str_)
print(f"d type is : {array.dtype}")