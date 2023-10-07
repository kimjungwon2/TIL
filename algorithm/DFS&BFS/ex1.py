from collections import deque


def solution(maps):
    answer = 0

    answer = bfs(0, 0, maps)

    if (answer == 1):
        return -1

    return answer


def bfs(x, y, maps):
    n = len(maps)
    m = len(maps[0])

    queue = deque()
    queue.append((x, y))

    #상,하,좌,우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue

            if (maps[nx][ny] == 0):
                continue

            if (maps[nx][ny] == 1):
                maps[nx][ny] = maps[x][y]+1
                queue.append((nx, ny))

    return maps[n-1][m-1]
