from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

members = list(i for i in range(N))

comb = list(combinations(members, N//2))
min_value = 100

for i in comb:
    start, link = 0,0
    j = list(set(members)-set(i))

    for k in combinations(i,2):
        start+= S[k[0]][k[1]]
        start+= S[k[1]][k[0]]
    for l in combinations(j,2):
        link+= S[l[0]][l[1]]
        link+= S[l[1]][l[0]]

    min_value = min(min_value,abs(start-link))

print(min_value)