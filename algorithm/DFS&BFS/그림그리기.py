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

visited = [[False]*m for _ in range(n)]


def bfs(x, y):
    count = 1
    # 상,하,좌,우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0 <= nx < n and 0 <= ny < m):
                if (graph[nx][ny] == 1 and visited[nx][ny] == False):
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1

    return count


cnt = 0
max_v = 0

for i in range(n):
    for j in range(m):
        if (visited[i][j] == False and graph[i][j] == 1):
            visited[i][j] = True
            cnt += 1
            max_v = max(max_v, bfs(i, j))


print(cnt)
print(max_v)
