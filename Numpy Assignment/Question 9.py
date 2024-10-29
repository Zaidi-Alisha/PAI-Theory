import numpy as np

arr = np.arange(1, 26)
percentile = np.percentile(arr, 75)
print("Array: ", arr)
print(percentile)