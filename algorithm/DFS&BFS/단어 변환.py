from collections import deque


def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer


def bfs(begin, target, words):
    count = 0
    queue = deque()
    queue.append((begin, count))

    if (target not in words):
        return 0

    while queue:
        start, count = queue.popleft()

        for i in words:
            if (change(start, i) == True):
                if i == target:
                    return count+1
                else:
                    queue.append((i, count+1))


def change(word, change):
    length = len(word)
    diff = 0
    for i in range(length):
        if word[i] != change[i]:
            diff += 1

    if diff == 1:
        return True
    else:
        return False
