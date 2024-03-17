def canVisitAllRooms(rooms):
    visited = {}
    
    #v에 연결되어 있는 모든 vertax에 방문할거다.    
    def dfs(v):
        visited[v] = True
        for next_v in rooms[v]:
            if next_v not in visited:
                dfs(next_v)

    dfs(0)

    if visited == len(rooms):
        return True
    
    return False


rooms = [[1,3],[2,4],[0],[4],[],[3,4]]
print(canVisitAllRooms(rooms))