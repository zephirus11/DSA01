# eg; aaaaccbaa =>a4c2b1a2
# create a string temp = ""
# iterate the string
# check if the adjaccent char same or not
# if same then increase count if not then cnt = 1
# then add char with count in temp string
# return temp string

s = "abcccdabb"
ch = ''
temp = ""
cnt = 1
for i in range(1,len(s)):
    if(s[i-1] == s[i]):
        cnt+=1
        ch = s[i-1]
    else:
        if(ch == ''):
            ch = s[i-1]
        temp+=ch+str(cnt)
        ch = ''
        cnt = 1
temp+=ch+str(cnt)

print(temp)