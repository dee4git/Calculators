import math

meu = 80
kox = 3.9
eox = 8.85 * pow(10, -14)
tox = 10.5 * pow(10, -8)

cox = kox * eox / tox
beta = meu * cox * 1 * pow(10, 6)
print('beta = ', beta, '* 10^-6')
beta = 17201008
print('beta = ', beta, '* 10^-6')

vgs = 2
vt = 1
vgt = vgs - vt
print('vgt =', vgt)
ids = beta * vgt * vgt / 2
print('highest ids = ', round(ids, 2))
vds = [.2, .3, .4]
for i in vds:
    print('ids for', i, '=', round(beta * (vgt - i / 2) * i, 2))
