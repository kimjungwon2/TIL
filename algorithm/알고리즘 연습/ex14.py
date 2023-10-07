answer = 1


def solution(n, computers):
    global answer

    visited = n*[False]
    node = 0

    while True:
        dfs(computers, node, visited)

        if False in visited:
            node = visited.index(False)
            answer += 1
        else:
            break

    return answer


def dfs(computers, node, visited):
    global answer
    visited[node] = True

    for i, neighbor in enumerate(computers[node]):
        if (neighbor == 1 and i != node and visited[i] == False):
            dfs(computers, i, visited)

s = solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
print(s)