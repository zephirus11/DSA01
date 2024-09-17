d = {
    "love":[1,2,3,4,5],
    "hate":[6,7,8,9],
    "like":[0],
}

newList = [(k,v) for k,v in d.items()]
print(newList)