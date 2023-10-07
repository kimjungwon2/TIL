import sys
from collections import deque
import copy

input = sys.stdin.readline
N, M = map(int,input().split())
lab = [ list(map(int,input().split())) for _ in range(N)]

# 0, 1벽, 2바이러스
answer = 0
dx,dy=[0,0,1,-1],[1,-1,0,0]

def wall(x):
    global answer

    if(x==3):
        answer = max(answer, bfs())
        return
    
    for i in range(N):
        for j in range(M):
            if lab[i][j]==0:
                lab[i][j]=1
                wall(x+1)
                lab[i][j]=0

def bfs():
    queue =deque()

    size = 0
    lab2 = copy.deepcopy(lab)

    for i in range(N):
        for j in range(M):
            if lab2[i][j]==2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if lab2[nx][ny]==0:
                    lab2[nx][ny]=2
                    queue.append((nx,ny))

    for i in range(N):
        size+= lab2[i].count(0)
    
    return size

wall(0)
print(answer)