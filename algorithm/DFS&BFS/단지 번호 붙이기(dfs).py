import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip()))  for _ in range(N)]

visited = [[False]*N for _ in range(N)]

result = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = 0
each = 0

def dfs(x,y):
    global each

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if(0<=nx<N and 0<=ny<N):
            if(visited[nx][ny] == False and graph[nx][ny]==1):
                visited[nx][ny]=True
                each += 1
                dfs(nx,ny)
    
    return True



for i in range(N):
    for j in range(N):
        if(visited[i][j]==False and graph[i][j]==1):
            visited[i][j] = True
            each +=1
            dfs(i,j)
            count+=1
            result.append(each)    
            each = 0

result.sort()

print(count)

for i in result:
    print(i)

