n = int(input("enter number of entries \n"))
d= {}
cnt = 0
for i in range(n):
    user_input = input().split()
    d[user_input[0]] = user_input[1]

for i in range(len(d)):
    key_input = input()
    value = d.get(key_input)
    if(value):
        print(key_input+"="+ value)
    else:
        print("Not found")
