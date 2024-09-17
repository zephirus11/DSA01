l = [1, 2, 3, 4, 5]
key = int(input("enter the number to search \n",))
flag = False
s = 0
e = len(l)-1
while (s <= e):
    mid = (s+e)//2
    if (l[mid] == key):
        flag = True
        break
    if (l[mid] < key):
        s = mid+1
    if (l[mid] > key):
        e = mid-1
if(flag):
    print("Found")
else:
    print("Not found")
