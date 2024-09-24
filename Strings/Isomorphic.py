from collections import defaultdict
def isoMorphic(s,t):
    d1 = defaultdict(str)
    d2 = defaultdict(str)
    for i in range(len(s)):
        if(d1[s[i]] and d1[s[i]] != t[i]):
            return False
        if(d2[t[i]] and d2[t[i]] != s[i]):
            return False
        d1[s[i]] = t[i]
        d2[t[i]] = s[i]
    return True

s = input("enter s1 \n")
t = input("enter s2 \n")

print(isoMorphic(s,t))