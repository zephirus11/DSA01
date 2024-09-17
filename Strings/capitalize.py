def capitalize(s):
    temp = ""
    ans = ""
    for i in range(len(s)):
        if (s[i] != ' '):
            temp += s[i]
        else:
            x = temp[0].upper()
            y = temp[-1].upper()
            ans += x+temp[1:len(temp)-1]+y+" "
            temp = ""
    x = temp[0].upper()
    y = temp[-1].upper()
    ans += x+temp[1:len(temp)-1]+y
    return ans
s = "github has its copilot"
print(capitalize(s))
