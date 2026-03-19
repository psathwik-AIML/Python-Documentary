import numpy as np 
ran=np.random.default_rng()
print(ran.integers(1,4))
print("...............")
print(np.random.uniform())
array=np.array([1,2,3,4,5])
ran.shuffle(array)
print(f"shuffle array: {array}")
print(f"choice array: {ran.choice(array)}")