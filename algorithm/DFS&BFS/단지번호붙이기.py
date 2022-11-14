"""
1.아이디어
- 2중 for 1 && 방문 x => DFS 
- 찾은 값을 저장 후 정렬해서 출력

"""

import sys

input = sys.stdin.readline
N = int(input())

graph = [list(map(int, input().strip())) for _ in range(N)]
visited =[[False]*N for _ in range(N)]

result=[]
count = 0

def dfs(x,y):
    global count

    count+=1

    #상,하,좌,우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny] == 1 and visited[nx][ny]==False:
                visited[nx][ny] = True
                dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j]==False:
            visited[i][j] = True
            count = 0
            dfs(i,j)
            result.append(count)

result.sort()
print(len(result))

for i in result:
    print(i)

