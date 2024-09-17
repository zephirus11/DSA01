d = {
    'sanjeev': 32,
    'ravi': 10,
    'rajnish': 9,
    'yash': 2,
    'suraj': 15
}
# sorting by keys
# l = list(d.keys())
# l.sort()
# print(l)

# dnew = {i: d[i] for i in l}
# print(dnew)

# sort by values
# d = dict(w=10, p=0, o=2, k=19, m=4)
lval = list(d.values())
lkey = list(d.keys())
lval.sort()
dnew = {lkey[lval.index(i)]:i for i in lval}
print(dnew)


