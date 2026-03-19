import numpy as np
array=np.array([1,2,3])
np.save("data",array)
print("array is saved")

# loading saved data 
a=np.load("data.npy")
print(a)