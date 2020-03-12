import numpy as np

a = np.arange(5)
b = np.arange(5, 9)
print(a)
print(b)

print(np.hstack((a, b)))
print('----------')

a = np.array([[1], [2], [3]])
b = np.array([['a'], ['b'], ['c']])
print(a)
print(b)
print(np.vstack((a, b)))
