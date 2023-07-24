# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_version_1(A):
    # Implement your solution here
    n = len(A)
    if n == 0:
        return 0
    m = len(A[0])
    visited = [[False]*m for _ in range(n)]
    countries = 0

    def dfs(i, j, color):
        if i<0 or i>=n or j<0 or j>=m or visited[i][j] or A[i][j] != color:
            return
        visited[i][j] = True
        dfs(i+1, j, color)
        dfs(i-1, j, color)
        dfs(i, j+1, color)
        dfs(i, j-1, color)

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                countries += 1
                dfs(i, j, A[i][j])

    return countries

print(solution_version_1([[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]))

# DFS is perfect for this because it can help to explore all areas that can be reached
# from a starting point while avoiding revisiting any areas, thus keeping track of all distinct countries.
# In the above function, a visited matrix to track if a cell in the matrix has been visited before or not is maintained.
#
# It initializes the countries to 0.

# In the main for loop, for every cell in the matrix, if the cell is not visited,
# the countries count is incremented by 1 and call dfs from that cell.
#
# In the dfs function, it starts from a cell, and if the cell is in the matrix, not visited and has the same color,
# it is marked as visited and call dfs in all four directions.
#
# This solution works by essentially treating each "country" as a group of connected cells with the same color.
#
# By iterating over the cells, and each time a cell is encountered that has not been seen before,
# it must be the start of a new country.

# Thus, the country count is increased and then DFS is used to mark all cells in the same country as visited.
#
# The space complexity of this solution is O(NM) and the time complexity is also O(NM), which is quite high.
#
# However, given the constraint of the problem, an even more optimized solution may not be feasible.

def solution_version_2(A):
    n = len(A)
    if n == 0:
        return 0
    m = len(A[0])
    visited = [[False]*m for _ in range(n)]
    countries = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]  # right, down, left, up

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                countries += 1
                color = A[i][j]
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if x<0 or x>=n or y<0 or y>=m or visited[x][y] or A[x][y] != color:
                        continue
                    visited[x][y] = True
                    for dx, dy in directions:
                        stack.append((x+dx, y+dy))

    return countries

print(solution_version_2([[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]))

# The solution is approached using an iterative depth-first search (DFS) algorithm, designed to handle larger datasets.

# The script begins with initializing the length of the grid (n) and handling the case where the grid is empty.
# The width (m) of the grid is then defined based on the first row.
# A visited matrix of the same dimensions is initialized to keep track of cells that have been checked.
# Next, the number of countries is initialized to zero, and a list of possible directions for movement is defined.

# This list contains tuples representing right, down, left, and up directions.

# The script then moves into a nested loop, checking each cell of the grid.
# If a cell is encountered that hasn't been visited, the number of countries is incremented,
# indicating the start of a new country.
# The color of this starting cell is then stored.

# A stack data structure is then introduced, storing the coordinates of the starting cell.
# Until the stack is empty, the script continues to explore the grid.
# The topmost cell from the stack is popped, and its coordinates are examined.
# If these coordinates fall outside the grid boundaries,
# or if the cell has already been visited,
# or if the cell does not match the current country's color, the script continues to the next iteration.
#
# If the cell meets all the conditions, it is marked as visited.
# Then, for every direction in the defined list, a new cell is appended to the stack,
# which represents a cell in that direction from the current cell.
#
# Finally, after all cells have been checked, the total number of countries identified is returned.
#
# This solution provides an efficient way to solve the problem by minimizing the risk of stack overflow errors
# and carefully managing the cells to be visited using the stack data structure.