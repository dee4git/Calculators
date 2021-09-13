p = 1, .5, .1
q = .5, .8, .3
r = 0, 0, 1

a1 = .1
a2 = .3
a3 = 1 - a2 - a1

for p, q, r in zip(p, q, r):
    print(round((a1 * p + a2 * q + a3 * r), 2))
