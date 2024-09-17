# find maximum points of card that have k points in n element list
l = [96, 90, 41, 82, 39, 74, 64, 50, 30]
k = 8
# we will try to make window of four elements-:
# * 1st window is 1st four indices of list
# * 3 elements from 1st 3 indices and one from last index
# * 2 elements from 1st 2 indices and two from last indices
# * 1 element from 1st 1 index and three from last indices
# * all from last indices

lsum = 0
# calc lSum for first k elements (created first k window)
for i in range(k):
    lsum += l[i]

# now calc rSum by adding window from back and subtracting front window
i = k-1
index = len(l)-1
rsum = 0
maxSum = float('-inf')
while (i >= 0):
    lsum -= l[i]
    rsum += l[index]
    index -= 1
    i -= 1
    maxSum = max(maxSum, lsum+rsum)

print(maxSum)
