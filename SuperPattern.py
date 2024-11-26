N = int(input())
if (N >= 3 and N % 2 != 0):
    m = (N//2) + 1
    n = N//2
    for i in range(m):
        if (i == m-1):
            print(" " * (m-i) + "*" * (i+1) + "e" * (2 + N) + "*")
        else:
            print(" " * (m-i) + "*" * (i+1) + " " * (N+2) + "*")
    for i in range(n+1, -1, -1):
        if (i < 2):
            break
        print(" " * (n-i+3) + "*" * (i-1) + " " * (N+2) + "*")
else:
    print("Enter row greater than 3 and in odd number")
