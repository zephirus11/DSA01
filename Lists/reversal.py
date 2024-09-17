#   reversing inplace
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s = 0
# e = len(l)-1
# while (s <= e):
#     l[s], l[e] = l[e], l[s]
#     s = s+1
#     e = e-1

# print(l)

# slicing technique
# print(l[::-1])

# using reverse function
# l.reverse()
# print(l)
# print(list(reversed(l)))


# modification is to do with list comprehension
# we can traverse backwards 
# for this we can use for loop by any of the two methods
# 1)using the reversed keyword
# 2)using range with negative steps 
# revList = [i for i in reversed(l)]
# print(revList)
# normalList = [l[i] for i in range(len(l)-1,-1,-1)]
# print(normalList)
