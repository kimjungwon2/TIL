def solution(keyinput, board):
    limit_x = board[0]//2
    limit_y = board[1]//2

    x = 0
    y = 0

    for i in keyinput:
        if (i == "up"):
            if (-1*limit_y <= y < limit_y):
                y += 1
            elif (limit_y == y):
                y = limit_y
            else:
                continue

        elif (i == "down"):
            if (-1*limit_y < y <= limit_y):
                y -= 1
            elif (-1 * limit_y == y):
                y = -1*limit_y
            else:
                continue

        elif (i == "right"):
            if (-1*limit_x <= x < limit_x):
                x += 1
            elif (limit_x == x):
                x = limit_x
            else:
                continue

        elif (i == "left"):
            if (-1*limit_x < x <= limit_x):
                x -= 1
            elif (-1*limit_x == x):
                x = -1*limit_x
            else:
                continue

    answer = []

    answer.append(x)
    answer.append(y)

    return answer
