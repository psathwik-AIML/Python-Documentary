# aggregate functions  = summarize data and returns single value 
import numpy as np
array=np.array([[1,2,3],[4,5,6]])

print(f"sum :{np.sum(array)}")
print(f"mean :{np.mean(array)}")
print(f"standard deviation :{np.std(array)}")
print(f"variance:{np.var(array)}")
print(f"min :{np.min(array)}")
print(f"max :{np.max(array)}")
print(f"argmin:{np.argmin(array)}")
print(f"argmax:{np.argmax(array)}")

# sum across separate rows / columns 
print(f"columns : {np.sum(array,axis=0)}")
print(f"rows : {np.sum(array,axis=1)}")