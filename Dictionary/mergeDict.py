d1 = {}
d2 = {}
n = 10

for i in range(1, n+1):
    if (i <= 5):
        d1[i] = ' '+'a'
    if (i > 5):
        d2[i] = ' '+'b'

# print(d1)
# print(d2)
# # merge using unpacking
# print({**d1,**d2})

# # using | operator
# print(d2|d1)
