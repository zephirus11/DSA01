from collections import Counter
X = int(input())
shoe_size = map(int, input().split(" "))
N = int(input())
print( Counter(shoe_size))
