import numpy as np

def normalize(arr):
    return (arr - np.mean(arr)) / np.std(arr)

arr = np.array([12, 23, 34, 43, 52, 63])
normalized_array = normalize(arr)
print("Array:\n", arr)
print("Normalized Array:", normalized_array)
