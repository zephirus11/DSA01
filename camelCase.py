s = input()
wrd = ""
for i in range(len(s)):
    if s[i].islower():
        wrd+=s[i].upper()
    if s[i].isupper():
        wrd = ""
        wrd+=s[i].lower()
        
    print(wrd)