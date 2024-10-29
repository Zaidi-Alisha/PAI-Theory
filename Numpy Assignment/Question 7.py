import numpy as np

arr = np.random.rand(50)
max = np.argmax(arr)
min = np.argmin(arr)
print("Array: ", arr)
print("Max value index:", max)
print("Min value index:", min)
