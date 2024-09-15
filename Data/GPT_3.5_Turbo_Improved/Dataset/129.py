def minPath(grid, k):
    n = len(grid)

    val = min(min(row) for row in grid)  # Find the minimum value in the grid

    ans = []
    for i in range(k):
        if i % 2 == 0:
            ans.append(min(grid[i % n]))  # Append minimum value
        else:
            ans.append(val)  # Append overall minimum value
    return ans
