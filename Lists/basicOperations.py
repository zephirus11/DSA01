l = []
l2 = [1, 2, 3, 4, 56]
l3 = list([])

# print(l, l2, l3)

for i in range(int(input())):
    l2.append(i)
    l2.insert(i+1, i+2)
    if i % 2 != 0:
        l2.remove(i)

print(l2)

# LIST = [i**2 for i in range(1, int(input())+1)]
# print(LIST)
