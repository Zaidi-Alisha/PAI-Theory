import numpy as np

mat = np.random.randint(1, 10, (3, 3))
constants = np.array([4, 6, 3])
result = np.linalg.solve(mat, constants)
print("Matrix:\n", mat)
print("Answer:", result)