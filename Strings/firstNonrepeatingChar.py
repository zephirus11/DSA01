# TO FIND FIRST NON REPEATING CHAR
# brute force approach
from collections import defaultdict
s = "approach"
d = defaultdict(int)
for i in s:
    d[i]+=1
u_key =''
for k,v in d.items():
    if(v == 1):
        u_key = k
        break

for index,element in enumerate(s):
    if(u_key == element):
        print(index)
        break

# from collections import defaultdict
# s = "approach"
# d = defaultdict(int)
# for i in s:
#     d[i] += 1
# cnt = 0
# for k, v in d.items():
#     if (v == 1):
#         print(cnt, "with", k)
#         break
#     cnt += 1


