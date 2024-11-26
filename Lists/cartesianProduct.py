l1 = ["1", "2"]
l2 = ["a", "b"]
# lans = [1a,1b,2a,2b]
List = [int(l1[i]) * l2[j] for j in range(len(l2)) for i in range(len(l1))]

print(List)

# list comprehensions advanced
# l = [expression for element in iterable if(condition)]
#  syntax tells that for every element in iterable render that expression which follows the condition

la = ["a", "b"]
lb = [1, 2]
l = [la[x] * lb[y] for x in range(len(la)) for y in range(len(lb))]
print(l)
