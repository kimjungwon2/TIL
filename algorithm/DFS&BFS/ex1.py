import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]


def bfs(x, y):
    queue = deque()
    size = 1
    queue.append((x,y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0 <= nx < n and 0 <= ny < m):
                if (visited[nx][ny] == False and picture[nx][ny] == 1):
                    visited[nx][ny] = True
                    size += 1
                    queue.append((nx, ny))

    return size


max_size = 0
count = 0

for i in range(n):
    for j in range(m):
        if (visited[i][j] == False and picture[i][j] == 1):
            visited[i][j] = True
            max_size = max(bfs(i, j), max_size)
            count += 1

print(count)
print(max_size)
