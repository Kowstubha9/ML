import numpy as np

# Creating a NumPy array from a Python list
ar1 = np.array([15, 52, 23, 84, 5])
print(ar1)

# Element-wise operations
arr1 = np.array([21, 25, 35])
arr2 = np.array([44, 5, 56])
#Addition
sum_res = arr1 + arr2
print(sum_res)
print(np.add(arr1,arr2))

ar1=np.array([15,21,6])
# Mathematical functions
sin_values = np.sin(ar1)
print("Sine values of the given array:")
print(sin_values)
print("Tan values of the given array:")
tan_values = np.tan(ar1)
print(tan_values)

# Linear algebra operations
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(m1, m2)
print(dot_product)

ar1 = np.array([15, 52, 23, 84, 5])

# Indexing
print(ar1[0])  # Accessing the first element

# Slicing
print(ar1[1:4])  # Accessing elements from index 1 to 3

ar1 = np.array([15, 52, 23, 84, 5])

# Shape of an array
print(ar1.shape)

# Reshaping
reshaped_ar1 = ar1.reshape(5, 1)
print(reshaped_ar1)
