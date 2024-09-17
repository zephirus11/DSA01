# brute force
def rev(s,ans,var):
    if(len(ans) == len(s)):
        print(ans)
        return
    ans+=s[var]
    rev(s,ans,var-1)
    

s = input("enter the string to reverse it \n")
rev(s,"",-1)

# using inbuilt function
# def reverse(s, ans):
#     if (len(ans) > 0):
#         print(ans)
#         return
#     ans = s[::-1]
#     reverse(s, ans)
# reverse("Aradhya", "")

