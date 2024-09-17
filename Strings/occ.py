# # counting occurences of chars in string

# # brute force O(N*N)
# name = "aradhya"
# for i in range(len(name)):
#     j = 0
#     count = 0
#     for j in range(len(name)):
#         if(name[i] == name[j]):
#             count+=1

#     print(f'count of {name[i]} is {count}')

# # through counter method O(N+M) M ARE UNIQUE CHARS
# from collections import Counter
# string = input()
# d ={}
# for i in range(len(string)):
#     d[i] = string[i]

# occ = Counter(d.values())
# print(occ)


# modification to count number of substr in a string

