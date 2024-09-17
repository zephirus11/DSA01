# def isPal(s, n, start, end, flag):
#     if (start >= end):
#         if (flag):
#             print("it is Palindrom")
#         else:
#             print("Not a palindrome")
#         return
#     if (s[start] == s[end]):
#         flag = True
#     else:
#         flag = False
#     isPal(s, n, start+1, end-1, flag)


# s = "RACECAR"
# isPal(s, len(s), 0, len(s)-1, False)

# using functional recursion
def Pal(s, n, start):
    if (start >= n/2):
        return True
    if (s[start] != s[n-start-1]):
        return False
    return Pal(s, n, start+1)


print(Pal("RACECAR", len("RACECAR"), 0))
