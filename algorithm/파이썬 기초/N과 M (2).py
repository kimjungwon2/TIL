from itertools import combinations

N, M = map(int, input().split())

arr = [str(i) for i in range(1, N+1)]


a = list(combinations(arr, M))

for i in a:
    print(' '.join(i))
