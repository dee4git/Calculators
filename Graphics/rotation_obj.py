import math

import numpy as np

theta = 45
sin_theta = round((np.around(np.sin(math.radians(theta)), decimals=5)), 2)
cos_theta = round((np.around(np.cos(math.radians(theta)), decimals=5)), 2)
h = -2
k = 3
R = np.array([
    [cos_theta, sin_theta, 0],
    [-sin_theta, cos_theta, 0],
    [0, 0, 1]
]
)
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
print('R')
print(R)
print('Tpos')
print(Tpos)
print('Tneg')
print(Tneg)
# print('obj coordinate: result without using origin point')
# print('---obj*R')
# print(obj.dot(R))

print('obj coordinate: result step by step using origin point')
print('--obj*Tneg')
print(obj.dot(Tneg))
print('--obj*Tneg*R')
print(obj.dot(Tneg).dot(R))
print('--obj*Tneg*R*Tpos')
print(obj.dot(Tneg).dot(R).dot(Tpos))
