l1 = ["1","2"]
l2 = ["a","b"]
# lans = [1a,1b,2a,2b]
List = [int(l1[i]) * l2[j] for j in range(len(l2)) for i in range(len(l1))]

print(List)