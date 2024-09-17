# find the max length of substr of atmost k distinct chars
# Brute force
from collections import defaultdict
s = "aaabbccd"
k = 2
maxLength = float('-inf')
for i in range(len(s)):
    d = defaultdict(int)
    for j in range(i, len(s)):
        d[s[j]] += 1
        if (len(d) <= k):
            maxLength = max(maxLength, j-i+1)
        else:
            break

print(maxLength)
# optimal solution
# r = 0
# l = 0
# while (r < len(s)):
#     d[s[r]] += 1
#     while (len(d) > k):
#         d[s[l]] -= 1
#         if (d[s[l]] == 0):
#             del d[s[l]]
#         l += 1
#     if (len(d) <= k):
#         maxLength = max(maxLength, r-l+1)

#     r += 1
# print(maxLength)