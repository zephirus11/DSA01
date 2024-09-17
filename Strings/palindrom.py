# method 1:
name = "MADAM RACECAR"
e = len(name)-1
flag = False
for i in range(len(name)):
    if (name[i] == name[e]):
        flag = True
    elif (name[i] != name[e]):
        flag = False
        break  # Exit the loop if a mismatch is found
    e = e-1
print(flag)


# method 2:
# name = "OPPO"
# name2 = name[::-1]
# if (name == name2):
#     print(True)
# else:
#     print(False)


# MODIFICATIONS CAN BE TO COUNT NUMBER OF OCCURENCES
