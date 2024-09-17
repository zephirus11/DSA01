# find the key with max value and min value 
# 1) to store the key and vals in two different list(lk,lv)
# 2) iterate in d of value to find min and max val from it
# 3) using lv.index() method find index of maxValue and minValue
# 4) wrap up the index in lk to find the key of those values

# d = {
#     "a":1,
#     "j":0,
#     "p":1100,
#     "v":-12,
#     "q":31,
#     "w":1101,
#     "h":19,
#     "b":143,
# }
# maxVal = float('-inf')
# minVal = float('inf')
# lv = list(d.values())
# lk = list(d.keys())
# for i in d:
#     maxVal = max(maxVal,d[i])
#     minVal = min(minVal,d[i])
#     maxKey = lk[lv.index(maxVal)]
#     minKey = lk[lv.index(minVal)]
    

# print(f'the key with max value in dictionary is {maxKey} and min val in dictionary is {minKey}')