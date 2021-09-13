import math

# test: https://www.rapidtables.com/convert/color/rgb-to-hex.html
import numpy as np

r = .55
g = .45
b = .2
up = (r - g) + (r - b)
down = (r - g) * (r - g) + (r - b) * (g - b)
print('up, down:', round(up, 2), round(down, 2))
theta = (.5 * up) / pow(down, .5)
print('theta =', round(theta, 2))
h = math.degrees(math.acos(theta))
print('theta degree=',  h)
if b > g:
    h = 360 - h
s = 1 - (3 * min(r, g, b) / (r + g + b))
i = (r + g + b) / 3
print('h =', round(h, 2))
print('s =', round(s, 2))
print('i =', round(i, 2))
