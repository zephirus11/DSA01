# d = {}
# flag = False
# for i in range(1, 10):
#     d[i] = i*10
#     if (i/4 in d.keys()):
#         flag = True
#     else:
#         flag = False
#         break

# print(flag)
# print(d)

# d = dict(one=1,two=2,three=3,four=4)
# flag = False
# user_input = input()
# for i in d:
#     if user_input in d.keys():
#         flag = True
#     else:
#         flag = False
#         break

# if(flag == True):
#     print("key present")
# else:
#     print("key is absent")

d = {
    "a":1,
    "b":2,
    "c":3,
}

user_input = input()
if(user_input in d):
    print("present")
else:    
    print("absent")