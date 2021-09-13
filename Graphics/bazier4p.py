p0 = 1, 2
p1 = 3, 8
p2 = 12, 13
p3 = 16, 4

t = .225

a = pow((1 - t), 3)
b = 3 * t * pow((1 - t), 2)
c = 3 * t * t * (1 - t)
d = 3 * t * t * t

for i, j, k, l in zip(p0, p1, p2, p3):
    print(round(a * i + b * j + c * k + d * l, 2))
