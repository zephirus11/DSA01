l = [2, 5, 7, 1, 8, 9]
k = 14
maxLength = float('-inf')

# for i in range(len(l)):
#     sum = 0
#     for j in range(i, len(l)):
#         if sum <= k:
#             sum += l[j]
#             if sum > k:
#                 break
#             maxLength = max(maxLength, j-i+1)

# print(maxLength)

# Sliding window technique
left = 0
right = 0
sum = 0
while (right < len(l)):
    sum = sum + l[right]
    while (sum > k):
        sum = sum-l[left]
        left += 1
    maxLength = max(maxLength, right-left+1)
    right = right+1
print(maxLength)
