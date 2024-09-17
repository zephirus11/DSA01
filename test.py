# brute force
l = []
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
for i in range(len(arr)):
    maxi = float('-inf')
    cnt = 0
    for j in range(i, len(arr)):
        cnt += 1
        if (arr[j] > maxi):
            maxi = arr[j]
        if (cnt == k):
            break
    l.append(maxi)
    if (arr[-1] == maxi):
        break
print(l)
# sliding window technique
# r = 0
# l = 0
# cnt = 0
# maxi = float('-inf')
# while (r < len(arr)):
#     if (cnt < k):
#         maxi = max(maxi, arr[r])
#         r += 1
#         cnt += 1
#     if (cnt == k):
#         cnt -= 1
#         l += 1
#         list.append(maxi)

# print(list)
