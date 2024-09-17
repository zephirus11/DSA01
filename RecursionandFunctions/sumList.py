def Sum(l, i, sum):
    if (i == 5):
        print(sum)
        return
    sum+=l[i]
    Sum(l,i+1,sum)


l = [1, 2, 3, 4, 5]
Sum(l, 0, 0)
