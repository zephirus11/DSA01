# first approach done by self
from collections import defaultdict
l = [1, 2, 4, 6, 3, 7, 8]
n = 8

xor = 0
for i in range(len(l)):
    xor^=l[i]

for i in range(1,n+1):
    xor^=i

print(xor)

# lnew = []
# for i in range(n):
#     lnew.append(i+1)
#     if (lnew[i] not in l):
#         print(f'{lnew[i]} is missing from l')
#         # break
# print(lnew)

# brute force Hashing
# d = defaultdict(int)
# for i in range(1, n+1):
#     d[i] += 1

# for k, v in d.items():
#     if (k not in l):
#         print(k)
# better approach
# sum = n*(n+1)//2
# lsum = 0
# for i in l:
#     lsum+=i
# print(f'{sum-lsum} is missing from list')

# optimal approach
# xor = 0
# for i in range(1, len(l)+1):
#     xor = xor ^ i
# print(xor)
# for i in l:
#     xor = xor ^ i

# print(xor)
