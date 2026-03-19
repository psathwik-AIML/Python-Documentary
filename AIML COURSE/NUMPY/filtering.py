# filtering means the process of selecting elements in array what matches given condition 
import numpy as np
array=np.array([[1,2,3],[4,5,6]])
print(array[array>4])

print("...................")
even=np.where(array%2==0,array,0)
print(even)