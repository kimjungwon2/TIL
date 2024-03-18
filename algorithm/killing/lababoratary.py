from collections import deque
import sys
import copy

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]



max_v = -1e10

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(lab):
    count = 0
    lab_copy = copy.deepcopy(lab)
    visited = [[False]*M for _ in range(N)]

    queue =deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append((i,j))
                visited[i][j]=True

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and lab_copy[nx][ny] == 0:
                lab_copy[nx][ny]=2
                queue.append((nx,ny))                    
                visited[nx][ny]=True
    
    for i in range(N):
        for j in range(M):
            if lab_copy[i][j] == 0:
                count+=1
    
    return count


def setWalls(graph,cnt):

    global max_v

    if cnt == 3:
        max_v = max(max_v,bfs(graph))
        return
    

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j]=1
                setWalls(graph,cnt+1)
                graph[i][j]=0

setWalls(graph,0)

print(max_v)

