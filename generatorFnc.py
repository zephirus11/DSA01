def fibo():
    a, b = 0, 1
    sum = 0
    while True:
        yield sum
        sum, a, b = b, b, a+b


f1 = fibo()  # f1 is now an iterator
print(next(f1))  # to iterate we can use next keyword
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
