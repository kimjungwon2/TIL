from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip()))  for _ in range(N)]

visited = [[False]*N for _ in range(N)]

result = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph,x,y):
    queue =deque()
    queue.append((x,y))

    visited[x][y] = True
    count = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    count+=1

    return count


for i in range(N):
    for j in range(N):
        if visited[i][j] == False and graph[i][j] == 1:
            result.append(bfs(graph,i,j))


result.sort()

print(len(result))

for i in result:
    print(i)