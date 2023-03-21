from collections import deque


def solution(maps):
    answer = 0

    answer = bfs(maps)

    if (answer == 1):
        return -1
    else:
        return answer


def bfs(maps):
    n_x = len(maps)
    n_y = len(maps[0])

    queue = deque()
    queue.append((0, 0))

    #상,하,좌,우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y+dy[i]

            if (0 <= nx < n_x and 0 <= ny < n_y):
                if (maps[nx][ny] == 1):
                    maps[nx][ny] = maps[x][y]+1
                    queue.append((nx, ny))

    return maps[n_x-1][n_y-1]
