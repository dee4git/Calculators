import math
import numpy as np

# test: https://www.rapidtables.com/convert/color/rgb-to-hex.html
h = 274
s = .89
i = .94
x = h
if 120 <= h < 240:
    h = h - 120
if h >= 240:
    h = h - 240

print('h=', h)
up = s * (np.around(np.cos(math.radians(h)), decimals=5))
down = (np.around(np.cos(math.radians(60 - h)), decimals=5))
print('up, down=', up, down)
one = i * (1 - s)
two = i * (1 + up / down)
three = 3 * i - (one + two)
print('for  --> up, down: ', up, down)
if x < 120:
    print('b =', round(one, 2))
    print('r =', round(two, 2))
    print('g =', round(three, 2))

if 120 <= x < 240:
    print('r =', round(one, 2))
    print('g =', round(two, 2))
    print('b =', round(three, 2))

else:
    print('g =', round(one, 2))
    print('b =', round(two, 2))
    print('r =', round(three, 2))
