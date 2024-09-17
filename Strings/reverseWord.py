# WRD = "I am a BOY" >> BOY a am I
# Brute force
# string = input("enter the sentence to reverse it \n")
# temp = ""  # created empty string to store each word on iteration
# l = []  # to store full string.
# for i in range(len(string)):
#     if (string[i] != ' '):  # when there is no space this means a word can be extracted and stored in temp
#         temp += string[i]
#     else:
#         # when a space is encountered then word can be appended to list
#         l.append(temp)
#         temp = ""  # emptying temp to store next word
# l.append(temp)  # handling the last word out of loop
# l.reverse()
# ans = " ".join(l)  # converting list to string
# print(ans)

# index insertions
# optimized approach tc:O(n) sc:O(n)
arr = ["I", "need", "you", "stay"]
ans = []
index = 0
for i in arr:
    ans.insert(index, i)
print(" ".join(ans))
