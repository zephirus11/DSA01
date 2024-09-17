def chkPrime(n):
    if (n < 2):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    
    return True

n = int(input())

for i in range(n+1):
    if(chkPrime(i)):
        print(i)
    
    
l = [i for i in range(n+1) if(chkPrime(i))]
print(l)