import numpy as np
import matplotlib as plt


v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

print(v1,v2)

# ------

v3 = np.array([[1],[2],[3]])
v4 = np.array([[4],[5],[6]])

print(v1,v2)

# ------ Matrix -----

v5 = np.array([[1,2],[3,4]])
v6 = np.array([[5,6],[7,8]])

print(v5,v6) 


# ------ Matrix Operations -----

m_sum = v1 + v2
m_min = v1 - v2

print("Soma: ", m_sum)
print("Sub: ", m_min)


mul_mat = np.dot(v1, v2)
print("Mul: ", mul_mat)

# Matrix identity
m_iden = np.eye(2)
print("Matrix identity: ", m_iden)


# Transpose matrix:
m_trans = np.transpose(v1)
print("Transposed:", m_trans)


# Complexy Numbers
complex1 = np.array([[1 + 2j, 3 + 4j], [5 + 6j, 7 + 8j]])
complex2 = np.array([[1 - 2j, 3 - 4j], [5 - 6j, 7 - 8j]])

print("Complexy:", complex1, complex2)

# Matrix Transposed and conjuged
# conjugation: basically will change the signal, like: 1 + 2j => 1 - 2j
matrix_conjuged = np.conjugate(np.transpose(complex1))
print("Matrix transposed and conjuged", matrix_conjuged)

# Trace of Matrix
tr = np.trace(v5)
print("Trace matrix:", tr)