import numpy as np

mat = np.random.randint(1, 10, (2, 2))
det = np.linalg.det(mat)
inverse = np.linalg.inv(mat)
print("Matrix:\n")
print(mat)
print("Determinant:")
print(det)
print("Inverse:")
print(inverse)