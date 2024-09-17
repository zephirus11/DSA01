# approach 1
s1 = input("enter the first string \n")
s2 = input("enter the second string \n")
# ans = sorted(s1)
# temp = sorted(s2)
# flag = True
# for i in range(len(ans)):
#     if(ans[i] != temp[i]):
#         flag = False

# print(flag)
flag = False
for i in range(max(len(s1),len(s2))):
    if(s1[i] in s2):
        flag = True
    else:
        flag = False
        break

print(flag)

# how to optimize
