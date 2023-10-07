from collections import deque


def solution(n, computers):
    answer = 0

    visited = [False]*(n+1)

    for i in range(n):
        if (visited[i] == False):
            bfs(i, computers, visited)
            answer += 1

    return answer


def bfs(node, computers, visited):
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()

        for index, i in enumerate(computers[node]):
            if (visited[index] == False and i == 1):
                visited[index] = True
                queue.append(index)

    return 0
