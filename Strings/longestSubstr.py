# longest substr with non repeating characters
# brute force O(n*n)
from collections import defaultdict
s = "GEEKSFORGEEKS"
maxLength = float('-inf')
for i in range(len(s)):
    temp = ""
    d = {}
    for j in range(i, len(s)):
        if (s[j] in d):
            break
        temp += s[j]
        d[s[j]] = 1
        maxLength = max(maxLength, j-i+1)
    # max Substring
    if(len(temp) >= maxLength):
        print(temp)

print(maxLength)


# Optimized approach O(N)
# s = "cadbzabcd"
# l = 0
# r = 0
# dict = defaultdict(int)
# maxLen = float('-inf')
# while (r < len(s)):
#     if (s[r] in dict):
#         if (dict[s[r]] >= l):
#             l = dict[s[r]]+1
#     dict[s[r]] = r
#     maxLen = max(maxLen, r-l+1)
#     r += 1

# print(maxLen)
