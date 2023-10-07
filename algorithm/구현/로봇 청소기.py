import sys
input = sys.stdin.readline
N,M = map(int,input().split())
x, y, d = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
#청소 개수
count = 0 

# 위,오,아래,좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while(True):
    if graph[x][y] == 0:
        graph[x][y]=2
        count+=1 
    sweap = False
    for i in range(1,5):
        nx = x+dx[d-i]
        ny = y+dy[d-i]

        if(0<=nx<N and 0<=ny<M):
            if(graph[nx][ny] == 0):
                d= (d-i+4)%4
                y= ny
                x = nx
                sweap = True
                break

    if sweap ==False:
        nx = x-dx[d]
        ny = y-dy[d]
        if (0 <= nx < N and 0 <= ny < M):
            if(graph[nx][ny]==1):
                break
            else:
                x = nx 
                y = ny
        else:
            break


print(count)