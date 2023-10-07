from collections import deque
import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

answer = 0

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]


def bfs():
    
    queue = deque()
    lab2 = copy.deepcopy(lab)

    #바이러스 있는 곳부터 시작
    for i in range(N):
        for j in range(M):
            if lab2[i][j] == 2:
                queue.append((i, j))

    while queue:
        px, py = queue.popleft()

        for k in range(4):
            nx = px+dx[k]
            ny = py+dy[k]
            if (0 <= nx < N and 0 <= ny < M):
                if lab2[nx][ny] == 0:
                    lab2[nx][ny] = 2
                    queue.append((nx, ny))

    global answer
    cnt = 0
    for i in range(N):
        cnt += lab2[i].count(0)

    answer = max(answer, cnt)


def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(cnt+1)
                lab[i][j] = 0


wall(0)
print(answer)
