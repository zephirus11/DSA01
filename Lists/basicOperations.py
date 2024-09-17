l = []
# l2 = [1, 2, 3, 4, 56]
l3 = list([])
print(l3)
# print(l, l2, l3)

for i in range(int(input())):
    l.append(i)
    l.insert(i+1, i+2)
    if i % 2 != 0:
        l.remove(i)

print(l)

# LIST = [i**2 for i in range(1, int(input())+1)]
# print(LIST)
