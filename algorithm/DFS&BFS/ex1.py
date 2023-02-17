import sys
from collections import deque 

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]


def bfs(x,y):
    result = 1
    queue = deque()
    queue.append((x,y))

    # 상, 하, 좌, 우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if(0<=nx<n and 0<=ny<m):
                if (graph[nx][ny] == 1 and visited[nx][ny] == False):
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    result+=1

    return result


count = 0
maxv = 0

for i in range(n):
    for j in range(m):
        if(graph[i][j]==1 and visited[i][j]==False):
            visited[i][j]=True
            count += 1
            maxv = max(maxv,bfs(i,j))


print(count)
print(maxv)

