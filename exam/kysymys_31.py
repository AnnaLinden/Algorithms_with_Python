# Given a matrix map (implemented in Python as a list of lists) 
# that represents a series of nodes and their connections 
# (two nodes are connected if they are neighbours, including diagonally). 
#  a function that finds the number of independent groups of nodes. 
# 1 or more nodes are independent if they are not connected with other nodes.

def DFS(coord, visited, map):
    # coord is a tuple with map's indices (row, col)
    # Directions are an array of tuples representing the 8 possible moves (including diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    stack = [coord]
    
    while stack:
        (row, col) = stack.pop()
        if visited[row][col]:
            continue
        visited[row][col] = True
        
        # Check all possible directions
        for d_row, d_col in directions:
            n_row, n_col = row + d_row, col + d_col
            # Check if the new position is inside the bounds and is part of a group
            if 0 <= n_row < len(map) and 0 <= n_col < len(map[0]):
                if map[n_row][n_col] == 1 and not visited[n_row][n_col]:
                    stack.append((n_row, n_col))

def get_groups(map):
    if not map:
        return 0
    
    rows = len(map)
    cols = len(map[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    group_count = 0
    
    for row in range(rows):
        for col in range(cols):
            if map[row][col] == 1 and not visited[row][col]:
                # New group found, perform DFS
                DFS((row, col), visited, map)
                group_count += 1
    
    return group_count

# Test case
# map_example = [
#     [1, 1, 1, 0, 1],
#     [1, 1, 0, 0, 1],
#     [0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 0],
#     [1, 1, 0, 0, 1]
# ]

# print(get_groups(map_example))  # Expected: 4
