def get_permutations(string, i=0):
    if (i == len(string)):
        print("".join(string))

    for j in range(i, len(string)):
        words = [char for char in string]
        words[i], words[j] = words[j], words[i]

        get_permutations(words, i+1)


get_permutations("yup")

# s = ["club", "clue", "club", "clutch"]
# s.sort()
# first = s[0]
# last = s[-1]
# wrd = ""
# for i in range(len(first)):
#     if(first[i] != last[i]):
#         print(wrd)
#         break
#     wrd+=first[i]

