n = 5
array = [1, 2, 3, 4, 3]

for num in array:
    index = abs(num) - 1
    if array[index] > 0:
        array[index] = -array[index]
    else:
        print(abs(num))
        