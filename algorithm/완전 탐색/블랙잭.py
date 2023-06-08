from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

comb = list(combinations(arr, 3))

MAX_VALUE = 0

for i in comb:

    if(sum(i)<=M):
        MAX_VALUE = max(MAX_VALUE, sum(i))


print(MAX_VALUE)
