def minPath(grid, k):
    n = len(grid)
    positions = {}  # To store the position (i, j) of each integer in the grid
    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)

    # Relative movements in the grid
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def min_adjacent_values(val):
        i, j = positions[val]
        adjacent_values = [grid[i + di][j + dj] for di, dj in deltas
                           if 0 <= i + di < n and 0 <= j + dj < n]  # Stay within the grid
        return min(adjacent_values) if adjacent_values else []

    ans = [1]
    for _ in range(1, k):
        next_val = min_adjacent_values(ans[-1])
        ans.append(next_val)

    return ans
