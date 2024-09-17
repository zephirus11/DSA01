# parameterized recursion
def sumDigit(n, sum):
    if (n == 0):
        print(sum)
        return
    sum += n % 10
    sumDigit(n//10, sum)


sumDigit(514, 0)
