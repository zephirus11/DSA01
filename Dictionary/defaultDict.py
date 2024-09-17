# finding frequency of letter in word
from collections import defaultdict

# below code is showing me the index of particular char
d = defaultdict(list)
wrd = "rreindeerrrr"
LIST = wrd.split()
for index,letter in enumerate(wrd):
    if letter == "r":
        d[letter].append(index)

print(d)

# for i in 'Mississippi':
#     d[i] += 1
# print(d)

# using normal dict
# d2 = {}
# for i in 'Mississippi':
#     if (i not in d2):
#         d2[i] = 1
#     else:
#         d2[i] += 1

# print(d2)
