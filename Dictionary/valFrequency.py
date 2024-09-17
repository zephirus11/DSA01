from collections import Counter
d = {}
for i in range(1, 10):
    if i < 3:
        d[i] = 'o'
    if i > 4 and i < 8:
        d[i] = 'a'
    if i >= 8:
        d[i] = 'k'

print(d)
fr = Counter(d.values())
print(dict(fr))
