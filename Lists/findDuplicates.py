# brute force
# to find duplicates what we basically do is to count the duplicates in list and store the count in a variable now whose count is more than one we take that element
# l = [1, 2, 3, 90, 0, 9, 0, 0, 1, 21, -1, -1]
# l = ["aradhya","radhya","radhya","a","b","aradhya"]
from collections import Counter, defaultdict
l = ["aradhya", "radhya", "b", "radhya", "araa",
     45, 0, 0, 100, "@", 45, "aradhya"]
d = {}
for i in l:
    if (i not in d):
        d[i] = 1
    d[i] += 1
    
print(d)

# s = set()
# for i in l:
#     j = 0
#     cnt = 0
#     for j in l:
#         if i == j:
#             cnt += 1
#             if(cnt > 1):
#                 s.add(j)

# print(s)

# optimized approach
# d = defaultdict(int)
# for i in range(len(l)):
#     d[i] = l[i]

# num = dict(Counter(d.values()))
# print(num)
# l2 = []
# for i in l:
#     n = l.count(i)
#     if (n > 1):
#         if(l2.count(i) == 0):
#             l2.append(i)

# print(l2)
