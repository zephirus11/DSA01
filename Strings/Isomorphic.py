from collections import defaultdict
s = "foo"
t = "bar"
flag = True
d1 = defaultdict(str)
d2 = defaultdict(str)
for i in range(len(s)):
    if(d1[s[i]] and d1[s[i]] != t[i]):
        flag = False
    if(d2[t[i]] and d2[t[i]] != s[i]):
        flag = False
    d1[s[i]] = t[i]
    d2[t[i]] = s[i]

print(flag)