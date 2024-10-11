from collections import Counter
X = int(input())
shoe_size = map(int, input().split())
avl = Counter(shoe_size)
num = int(input())
total_money = 0
for i in range(num):
    L = list(map(int, input().split()))
    if avl[L[0]] > 0:
        total_money += L[1]
        avl[L[0]] -= 1
print(avl)
print(total_money)