# brute force condition
l = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
lm = float('-inf')
# for i in range(len(l)):
#     cnt = 0
#     for j in range(i,len(l)):
#         if(l[j] == 0):
#             cnt+=1
#         if(cnt <= k):
#             lm = max(lm,j-i+1)
#         else:
#             break
# print(lm)

# optimized approach
right = 0
left = 0
zeros = 0
while (right < len(l)):
    if (l[right] == 0):
        zeros += 1
        if (zeros > k):
            while (l[left] != 0):
                left += 1
            zeros -= 1
            left += 1
    lm = max(lm, right-left+1)
    right += 1
print(lm)