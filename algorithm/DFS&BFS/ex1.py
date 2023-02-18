from collections import deque

graph = {
    'A':['B','D','E'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['A','B'],
    'E':['A']
}

def bfs(graph,start_v):
    queue = deque(start_v)
    visited=[start_v]

    while queue:
        current = queue.popleft()
        for next_v in graph[current]:
            if next_v not in visited:
                queue.append(next_v)
                visited.append(next_v)

    return visited