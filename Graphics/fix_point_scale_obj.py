import math

import numpy as np

h = 4
k = 4
sx = 2
sy = 2
S = np.array([
    [sx, 0, 0],
    [0, sy, 0],
    [0, 0, 1],
])
Tpos = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [h, k, 1],
])
Tneg = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [-h, -k, 1],
])
# row wise
obj = np.array([
    [3, 3, 1],
    [5, 4, 1],
    [4, 5, 1],
])
print('obj')
print(obj)
print('S')
print(S)
print('Tpos')
print(Tpos)
print('Tneg')
print(Tneg)
# print('obj coordinate: result without using origin point')
# print('---Obj*S')
# print(obj.dot(S))

print('obj coordinate: result step by step using origin point')
print('---obj*Tneg')
print(obj.dot(Tneg))
print('---obj*Tneg*S')
print(obj.dot(Tneg).dot(S))
print('---obj*Tneg*S*Tpos')
print(obj.dot(Tneg).dot(S).dot(Tpos))
