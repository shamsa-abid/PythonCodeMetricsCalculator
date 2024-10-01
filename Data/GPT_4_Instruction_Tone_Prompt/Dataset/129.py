def minPath(grid, k):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    path = []
    N = len(grid)
    cells = sorted((v, i, j) for i, row in enumerate(grid)
                   for j, v in enumerate(row))

    def dfs(i, j, remaining):
        if remaining == 0:
            return path[:]

        for dx, dy in moves:
            x, y = i + dx, j + dy
            if 0 <= x < N and 0 <= y < N and (x, y) not in visited:
                visited.add((x, y))
                path.append(grid[x][y])
                result = dfs(x, y, remaining - 1)
                if result:
                    return result
                visited.remove((x, y))
                path.pop()

    for _, i, j in cells:
        visited.add((i, j))
        path.append(grid[i][j])
        result = dfs(i, j, k - 1)
        if result:
            return result
        visited.remove((i, j))
        path.pop()