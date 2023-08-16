from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))

    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0 <= nx < N and 0 <= ny < M):
                if (graph[nx][ny] == 1 and visited[nx][ny] == False):
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y]+1

    return graph[N-1][M-1]


min_v = bfs(graph, 0, 0)

print(min_v)
