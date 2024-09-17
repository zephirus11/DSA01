# parameterized recursion
# def calc(x, n, ans):
#     if (n <= 0):
#         print(ans)
#         return
#     calc(x, n-1, ans*x)
# calc(7, 3, 1)

# functional recursion
def fnPow(n, k):
    if (k == n):
        return n
    return n*fnPow(n, k+1)


print(fnPow(5, 1))

