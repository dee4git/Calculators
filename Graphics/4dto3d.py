w = 15
p = 75, 90, 150, w
q = 100, 110, 150, w
r = 110, 110, 200, w
s = 110, 100, 200, w

p = [round(x / w, 2) for x in p]
q = [round(x / w, 2) for x in q]
r = [round(x / w, 2) for x in r]
s = [round(x / w, 2) for x in s]

print(p)
print(q)
print(r)
print(s)
