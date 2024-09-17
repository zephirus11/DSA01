# brute force
from collections import defaultdict
l = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
maxLength = 0
k = 2
# for i in range(len(l)):
#     d = defaultdict(int)
#     for j in range(i, len(l)):
#         d[l[j]] += 1
#         if(len(d) <= k):
#             maxLength = max(maxLength, j-i+1)
#         else:
#             break



# # optimized approach
# from collections import defaultdict
# right = 0
# left = 0
# d = defaultdict(int)
# while (right < len(l)):
#     d[l[right]] += 1
#     while (len(d) > k):
#         d[l[left]] -= 1
#         if(d[l[left]] == 0):
#             del d[l[left]]
#         left+=1
#     if(len(d) <= k):
#         maxLength = max(maxLength, right-left+1)
#         right += 1

# print(maxLength)
