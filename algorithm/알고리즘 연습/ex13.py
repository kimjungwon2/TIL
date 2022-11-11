from collections import deque


def solution(priorities, location):
    answer = 0
    length = len(priorities)
    a = []
    b = []

    for i in range(length):
        a.append((priorities[i], i))

    max_value = max(a)

    print(a)

    while (len(a) > 0):
        find = 0
        for i in a:
            if (i == max(a)):
                a.remove(i)
                b.append(i)
                find = 1
            elif (find == 1):
                a.remove(i)
                b.append(i)

    print(b)

    return answer


solution([1, 1, 9, 1, 1, 1], 0)
