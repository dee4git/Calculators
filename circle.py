from math import sqrt

h, k = 3, 3
r = 2


def coordinate(x, y):
    sqr = (x - h) * (x - h) + (y - k) * (y - k)
    sqr = round(sqrt(sqr))
    if sqr == r:
        print(x, y)


for i in range(8):
    for j in range(8):
        coordinate(i, j)
