# brute force nested list
# using two loops and then flattening
# l = []
# lans = []
# n = 5
# for i in range(n):
#     l2 = []
#     for j in range(i+1):
#         l2.append(j)
#     l.append(l2)  # nested list
#     for k in l2:
#         lans.append(k)
# print(lans)
# print(l)

# # optimized solution
# n=5
# NESTEDLIST = [[j for i in range(3)] for j in range(n)]
# print(NESTEDLIST)


# modifications attempt hackrnk questions in nested list

# for flattening the list the inner loop will be on extreme RHS (inner loop decides what to print)
# # for nesting the list the outer loop will be on EXTREME RHS (outer loop decides how many times run the inner loop)
# REMEMBER THE TYPE OF VALUES TO BE PRINTED BY QUALITY LOOP SO FOR NESTING WE USE QUALITY LOOP INSIDE AND QUANTITY LOOP(how much values to be printed) outside and vice versa for flattening the list
# LIST = [[j for j in range(5)] for i in range(3)]
# print(LIST)
# LIST = [j for i in range(3) for j in range(5)]
# print(LIST)

l = [[1, 2], [3, 4], [4, 5]]
lflat = []
for i in range(len(l)):
    for j in l[i]:
        lflat.append(j)

print(lflat)
