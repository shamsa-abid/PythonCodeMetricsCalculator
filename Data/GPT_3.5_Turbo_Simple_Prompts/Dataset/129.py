def minPath(grid, k):
    n = len(grid)

    def dfs(i, j, path):
        if len(path) == k:
            return path

        lowest = float('inf')
        next_cell = None

        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < n and 0 <= y < n and (x, y) not in path:
                if grid[x][y] < lowest:
                    lowest = grid[x][y]
                    next_cell = (x, y)

        path.append(grid[next_cell[0]][next_cell[1]])

        return dfs(next_cell[0], next_cell[1], path)

    min_val = float('inf')
    start = None

    for i in range(n):
        for j in range(n):
            if grid[i][j] < min_val:
                min_val = grid[i][j]
                start = (i, j)

    return dfs(start[0], start[1], [min_val])


# Example usage
grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k1 = 3
print(minPath(grid1, k1))  # Output: [1, 2, 1]

grid2 = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
k2 = 1
print(minPath(grid2, k2))  # Output: [1]
