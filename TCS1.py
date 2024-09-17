# s = input()
# cp = 0
# cn = 0
# for i in range(len(s)):
#     if (s[i] == "*"):
#         cp+=1
#     else:
#         cn+=1

# print(cp-cn)

# l = [10, 4, 8, 2, 9]
# cnt = 1
# for i in range(1,len(l)):
#     j = 0
#     while(j != i):
#         if(l[j] > l[i]):
#             cnt+=1
#         j+=1
# print(cnt)


# e = [7,0,5,1,3]
# l = [1,2,1,3,4]
# totalGuest = 0
# maxGuest = 0
# for i in range(len(e)):
#     totalGuest += e[i] - l[i]
#     maxGuest = max(maxGuest,totalGuest)
# print(maxGuest)

from collections import Counter
b = ['r', 'g', 'b', 'b', 'g', 'y', 'y', 'p']
d = {}
for i in range(len(b)):
    if (b[i] not in d):
        d[b[i]] = 0
    d[b[i]] += 1
isOdd = ''
for k, v in d.items():
    if (v % 2 != 0):
        isOdd += k + ' '
    if (v % 2 == 0):
        continue
print(isOdd, "are odd number of balloons")
