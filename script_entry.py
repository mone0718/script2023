import numpy as np

mat1 = np.array([[ 1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6 ]])
mat2 = np.array([[5, 3, 6, 7], [4, 2, 8, 1], [8, 0, 1, 4], [7, 2, 9, 2]])

mat3 = np.dot(mat1, mat2)

print(mat3)
