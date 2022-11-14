"""
아이디어 
- 2중 for 문  => 값 1 && 방문 X = > BFS
- BFS 돌면서 그림 개수+1,최대값 갱신 

시간 복잡도
노드 : m*n
e :v*4

"""

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))



visited = [[False] * m for _ in range(n)]


#상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    result = 1
    q = deque()
    q.append((x,y))
    while q:
        ex,ey = q.popleft()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]

            if 0 <= ny < m and 0 <= nx < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    result += 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
    return result


count = 0
max_v = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            count += 1
            max_v = max(max_v, bfs(i, j))

print(count)
print(max_v)
