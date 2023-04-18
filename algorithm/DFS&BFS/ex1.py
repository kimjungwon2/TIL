def solution(board):
    answer = 0
    warning = [[True]*len(board) for _ in range(len(board))]

    #상,하,좌,우
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for x in range(len(board)):
        for y in range(len(board)):
            if (board[x][y] == 1):
                warning[x][y] = False

                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if (0 <= nx < len(board) and 0 <= ny < len(board)):
                        warning[nx][ny] = False

    for i in warning:
        for j in i:
            if (j == True):
                answer += 1

    return answer
