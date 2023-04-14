from collections import deque

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}


def bfs(graph, start):
    queue = deque(start)
    visited = [start]

    while queue:
        v = queue.popleft()

        for next in graph[v]:
            if next not in visited:
                queue.append(next)
                visited.append(next)

    return visited


bfs(graph, 'A')

print(bfs(graph, 'A'))
