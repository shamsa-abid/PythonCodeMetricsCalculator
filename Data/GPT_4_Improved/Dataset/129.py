def minPath(grid, k):
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n = len(grid)
    target = min(min(grid))
    result = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == target:
                next_min = float("inf")
                for d in neighbors:
                    nx, ny = i + d[0], j + d[1]

                    if nx >= 0 and ny >= 0 and nx < n and ny < n:
                        next_min = min(next_min, grid[nx][ny])
                break

    for i in range(k):
        result.append(target if i % 2 == 0 else next_min)

    return result
