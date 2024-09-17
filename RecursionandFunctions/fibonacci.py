# without recursion
# a = 0
# b = 1
# sum = 0
# l = []
# for i in range(8):
#     if(a == 0 and b == 1):
#         l.append(a)
#         l.append(b)
#     sum = a+b
#     a = b
#     b = sum
#     l.append(sum)
# print(l)

# recursive solution
def fib(n,l):
    if (n <= 1):
        return n
    return fib(n-1)+fib(n-2)
print(fib(6))
