from collections import Counter


def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    stack = []

    j = 1

    while (100 > progresses[0] + speeds[0]*j):
        j += 1

    stack.append(j)
    print(stack)

    for i in range(1, length):
        j = 1

        while (100 > progresses[i] + speeds[i]*j):
            j += 1

        if (stack[-1] >= j):
            stack.append(stack[-1])
        else:
            stack.append(j)

    c = Counter(stack)

    s_values = c.values()

    for i in s_values:
        answer.append(i)

    return answer
