import numpy as np   # importing numpy library

# Create a 4x5 array filled with 0s
array = np.zeros((4, 5))
print(array)
print(".......................")

# Create a 3x5 array filled with 1s
array = np.ones((3, 5))
print(array)
print(".......................")

# Create a 4x4 array filled with value 31
array = np.full((4, 4), 31)
print(array)
print(".......................")

# Create a 6x6 identity matrix (diagonal = 1, rest = 0)
array = np.eye(6)
print(array)
print(".......................")

# Create a 4x2 array with random (uninitialized) values
# Values may be garbage (whatever is in memory)
array = np.empty((4, 2))
print(array)
print(".......................")

# Create an array from 1 to 50 (50 not included)
array = np.arange(1, 51)
print(array)
print(".......................")

# Create 7 evenly spaced values between 3 and 10
array = np.linspace(3, 10, 7)
print(array)
print(".......................")