d = {
    1: 'a',
    2: "b",
    3: "c"
}


# O(N) brute force
# d2 = {}
# for key, value in d.items():
# d2[value] = key
# print(f'{d} INVERTED DICTIONARY->>> {d2}')


# d.clear()

print(d)
dnew = {v:k for k,v in d.items()}
print(dnew)
# dnew = {v: k**2 for k, v in d}
# print(dnew)
