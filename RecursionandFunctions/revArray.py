# reverse array using recursion

# using two variables
def revArray(l, n, i, x):
    if (i >= x):
        print(l)
        return
    temp = x
    l[i], l[temp] = l[temp], l[i]
    revArray(l, n, i+1, x-1)


l = [1, 2, 3, 4, 5]
revArray(l, len(l), 0, len(l)-1)

# using one variable
def revSingle(l, n, i):
    if (i >= n-i-1):
        print(l)
        return
    l[i], l[n-i-1] = l[n-i-1], l[i]
    revSingle(l, n, i+1)

l = [1, 2, 3, 4]
revSingle(l, len(l), 0)
