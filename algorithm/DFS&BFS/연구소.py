from collections import deque
import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


# 1:벽 2: 바이러스

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph):
    queue = deque()

    graph2 = copy.deepcopy(graph)
    
    for i in range(N):
        for j in range(M):
            if graph2[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                
                if graph2[nx][ny] == 0 :
                    graph2[nx][ny] = 2
                    queue.append((nx, ny))
    
    return countSafe(graph2)


max_v = -1e9


def buildWall(graph, count):
    global max_v
    if (count == 3):
        max_v = max(bfs(graph), max_v)
        return max_v

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                buildWall(graph, count+1)
                graph[i][j] = 0


def countSafe(graph):

    count = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                count += 1

    return count


buildWall(graph, 0)
print(max_v)
