import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int,input().split())

lab = [list(map(int, input().split())) for _ in range(N)]


#1=> 퍼지지 못함.
#0=> 퍼진다.

def bfs(x,y):
    size = 1

    queue = deque((x,y))

    dx,dy=[0,0,1,-1],[-1,1,0,0]

    while queue:

        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if lab[nx][ny]==0:
                    lab[nx][ny]=2
                    size+=1
                    queue.append((nx,ny))

    return size

def wall(cnt,x,y):

    if(cnt==3):
        bfs(x,y)
        return 

    for i in range(N):
        for j in range(M):
            if lab[i][j]==0:
                lab[i][j]=1
                wall(cnt+1,x,y)
                lab[i][j]=0


wall(0)

    

