# remove duplicate preserved order of elements
def removeDuplicate(l):
    l2 = []
    for i in l:
        n = l.count(i)
        if n > 1:
            if l2.count(i) == 0:
                l2.append(i)
    return l2


print(removeDuplicate([211, 2, 2, 2, 1, 3, 1, 3, 211, 4, 15, 2]))


LIST = list([1, 4, 3, 4, 1, 12, 3, 2, 1, 2, 3, 2])
NEW_LIST = [] #this list will contain unique values from original list
for i in LIST:
    n = LIST.count(i) #counting the i value in list
    if n > 1: #check those values only whose count is greater than one/
        if NEW_LIST.count(i) == 0: #append those i values whose count is zero in new list.
            NEW_LIST.append(i)
print(NEW_LIST)