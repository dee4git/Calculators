import math

import numpy as np

h = 2
k = 2
sx = 2
sy = 2
S = np.array([
    [sx, 0, 0],
    [0, sy, 0],
    [0, 0, 1],
])
Tpos = np.array([
    [1, 0, h],
    [0, 1, k],
    [0, 0, 1],
])
Tneg = np.array([
    [1, 0, -h],
    [0, 1, -k],
    [0, 0, 1],
])
# col wise
obj = np.array([
    [1, 1, 3, 3],
    [1, 3, 3, 1],
    [1, 1, 1, 1],
])
print('obj')
print(obj)
print('S')
print(S)
print('Tpos')
print(Tpos)
print('Tneg')
print(Tneg)
print('wold coordinate: result without using origin point')
print('---S*obj')
print(S.dot(obj))

print('wold coordinate: result step by step using origin point')
print('---Tpos*S')
print(Tpos.dot(S))
print('---Tpos*S*Tneg')
print(Tpos.dot(S).dot(Tneg))
print('---Tpos*S*Tneg*obj')
print(Tpos.dot(S).dot(Tneg).dot(obj))
