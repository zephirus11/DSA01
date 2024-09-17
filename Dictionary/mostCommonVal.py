from collections import Counter
d = {
    "a": 1,
    "b": 2,
    "c": 1,
    "f": 10,
    "d": 2,
    "e": 2,
}
l = list(d.values())
print(l)
l2 = []
maxCount = float('-inf')
for i in l:
    cnt = l.count(i)
    maxCount = max(cnt,maxCount)

# counting the frequency of values in d
num = dict(Counter(d.values()))
print(num)
for key,val in num.items():
    if(val == maxCount):
        print(key)


