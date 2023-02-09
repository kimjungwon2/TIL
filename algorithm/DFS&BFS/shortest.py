from collections import deque

def shortest(grid):
    shortest_length = -1

    row = len(grid)
    col = len(grid[0])

    if grid[0][0]==1 and grid[row-1][col-1] == 1:
        return shortest_length
    
    visited = [[False]*col for _ in range(row)]

    delta = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    queue = deque((0,0,-1))
    visited[0][0]=True

    while queue:
        current_row, current_column, current_len = queue.popleft()

        if current_row == row-1 and current_column == col-1:
            shortest_length = current_len
            break
        
        for dr,dc in delta:
            next_r = current_row +dr
            next_c = current_column+dc
            if 0<=next_r<row and 0<=next_c<col:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    queue.append((next_r,next_c,current_len+1))
                    visited[next_r][next_c] = True
    
    return shortest_length

