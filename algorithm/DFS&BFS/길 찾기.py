import sys
from collections import deque

input =sys.stdin.readline

N, M = map(int, input().split())
board = [input() for _ in range(N)]

dx = [0,0,-1,1] 
dy = [-1,1,0,0]

def bfs():
    chk = [[False]*M for _ in range(N)]
    chk[0][0] = True

    queue= deque()

    queue.append((0,0,1))

    while queue:
        x,y,d = queue.popleft()

        if x==N-1 and y==M-1:
            return d

        nd= d+1 

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0<=nx<N and 0<=ny<M and board[nx][ny]=='1' and not chk[nx][ny]):
                chk[nx][ny]=True
                queue.append((nx,ny,nd))

print(bfs())