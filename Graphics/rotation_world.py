import math

import numpy as np

theta = 45
sin_theta = round((np.around(np.sin(math.radians(theta)), decimals=5)), 2)
cos_theta = round((np.around(np.cos(math.radians(theta)), decimals=5)), 2)
h = -2
k = 3
R = np.array([
    [cos_theta, -sin_theta, 0],
    [sin_theta, cos_theta, 0],
    [0, 0, 1]
]
)
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
    [3, 5, 4],
    [3, 4, 5],
    [1, 1, 1],
])
print('obj')
print(obj)
print('R')
print(R)
print('Tpos')
print(Tpos)
print('Tneg')
print(Tneg)
# print('wold coordinate: result without using origin point')
# print('---R*obj')
# print(R.dot(obj))

print('wold coordinate: result step by step using origin point')
print('---Tpos*R')
print(Tpos.dot(R))
print('---Tpos*R*Tneg')
print(Tpos.dot(R).dot(Tneg))
print('---Tpos*R*Tneg*obj')
print(Tpos.dot(R).dot(Tneg).dot(obj))
