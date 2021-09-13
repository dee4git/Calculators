p0 = 1, 2
p1 = 3, 8
p2 = 12, 13

t = .53

a = pow((1 - t), 2)
b = 2 * t * pow((1 - t), 1)
c = t * t

for i, j, k in zip(p0, p1, p2):
    print(round(a * i + b * j + c * k, 2))
