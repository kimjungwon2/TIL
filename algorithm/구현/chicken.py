import sys
from itertools import combinations

input = sys.stdin.readline

min_v = 999999
# 0:빈 칸, 1:집, 2: 치킨집.

N, M = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
distanceOfChicken =0
result = 999999

for i in range(N):
    for j in range(M):
        if (land[i][j] == 2):
            house.append((i+1, j+1))
        if (land[i][j] == 1):
            chicken.append((i+1, j+1))

for i in house:
    distanceOfChicken = 0
    for j in combinations(chicken, M):
        chi_len = 999
        for k in range(M):
            chi_len = min(abs(i[0]-j[k][0])+abs(i[1]-j[k][1]), min_v)
        distanceOfChicken += chi_len
    result = min(distanceOfChicken, result)

print(result)
