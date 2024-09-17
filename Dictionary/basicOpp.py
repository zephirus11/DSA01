d = dict(one=1, two=2, three=3)
print(d)
dic = {
    "name": "Hrithik",
    "Lname": "Yadav",
    "id": 123,
    "isStudent": "No"
}
# adding any key-value externally
dic["working"] = "Yes"
print(dic)
print(f'{dic.values()}, {dic.keys()}, {dic.items()}, {dic.pop("id")}')

# clear():clears all the key-values in dictionary(d.clear())
# copy():returns a shallow copy of dict . dict.copy()
# d.fromkeys() creates a dict from a given seq with val.(d.fromkeys(seq,val)) seq can be tuple,list
# d.get()gives value of given key
# d.items():gives k,v
# d.pop(key-name) return and remove the element from dictionary with given key
# d.popitem()-removes last key-value from dictionary
# d.setdefault(key-name,value):-sets key and value in dictionary,update(key-name:value):-changes the value of key
