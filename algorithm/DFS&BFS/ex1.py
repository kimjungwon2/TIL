from collections import deque
import sys

input =sys.stdin.readline

n, m = map(int,input().split())

picture = [ list(map(int, input().split())) for _ in range(n)]
visited = [m * [False] for _ in range(n)]


count = 0
maxv = 0 

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    size = 1

    dx = [-1,1,0,0 ]
    dy = [0,0,1,-1]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if(0<=nx<n and 0<=ny<m):
                if(picture[nx][ny]==1 and visited[nx][ny]==False):
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    size+=1

    return size

for i in range(n):
    for j in range(m):
        if(visited[i][j]==False and picture[i][j]==1):
            visited[i][j]=True
            maxv = max(maxv, bfs(i,j))
            count+=1

print(count)
print(maxv)