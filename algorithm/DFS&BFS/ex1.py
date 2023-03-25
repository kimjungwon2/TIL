def solution(array, commands):
    answer = []

    length = len(commands)

    for i in range(length):
        for j in range(3):
            if (j == 0):
                a = commands[i][j]
            elif (j == 1):
                b = commands[i][j]
            elif (j == 2):
                c = commands[i][j]
        d = sorted(array[a-1:b])
        answer.append(d[c-1])

    return answer
