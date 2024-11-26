# def test(l, val1, n):
#     ans = []
#     cnt1 = 0
#     cnt2 = 0
#     for i in range(n):
#         if(l[i] < val1):
#             cnt1+=1
#         if(l[i] > val1):
#             cnt2+=1
#     ans.append(cnt1)
#     ans.append(1)
#     ans.append(cnt2)
#     return ans

# print(test([21,0,8,6,9,-1,11,3], 9, 8))


def chkPrime(n):
    if(n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True
def printPrime(lim):
    for i in range(lim+1):
        if (chkPrime(i)):
            print(i)
print(printPrime(20))
