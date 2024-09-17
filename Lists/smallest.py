def largest(l, maxi):
    for i in l:
        if i > maxi:
            maxi = i
    return f'the largest number in list is {maxi}'


def smallest(l, mini):
    for i in l:
        if (i < mini):
            mini = i
    return f'the smallest number in list is {mini}'


def secLargest(l, maxi, smax):
    for i in l:
        if (i > maxi):
            smax = maxi
            maxi = i
        elif (i > smax and smax < maxi):
            smax = i
    return f'the second largest number in list is {smax}'


def secSmallest(l, mini, smin):
    for i in l:
        if (i < mini):
            smin = mini
            mini = i
        elif (i < smin and smin > mini):
            smin = i

    return f'the second smallest number in list is {smin}'


l = [-10, 2, 3, 4, 4, -1, -2, 6, 122, 2, 0, 3]
print(l)
print(largest(l, float('-inf')))
print(smallest(l, float('inf')))
print(secLargest(l, float('-inf'), float('-inf')))
print(secSmallest(l, float('inf'), float('inf')))


