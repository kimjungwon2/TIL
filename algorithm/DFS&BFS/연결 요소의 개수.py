import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
adj = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

ans = 0
chk = [False] * N


def dfs(now):
    for next in range(N):
        if adj[now][next] and not chk[next]:
            chk[next] = True
            dfs(next)


for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)
