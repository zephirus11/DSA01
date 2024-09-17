from collections import defaultdict
d = defaultdict(int)
for i in "belt":
    d[i] += 1

print(d)
d['o'] += (9)
print(d)
