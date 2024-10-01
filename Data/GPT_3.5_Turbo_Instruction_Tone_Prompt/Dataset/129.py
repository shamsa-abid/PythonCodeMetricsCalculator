
def minPath(grid, k):
    n = len(grid)
    values = [False] * (n * n + 1)
    path = []

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n

    def backtrack(x, y, step):
        nonlocal path

        if step == k:
            return True

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                val = grid[nx][ny]
                if not values[val]:
                    values[val] = True
                    path.append(val)
                    if backtrack(nx, ny, step + 1):
                        return True
                    path.pop()
                    values[val] = False

        return False

    for i in range(n):
        for j in range(n):
            values[grid[i][j]] = True
            path = [grid[i][j]]
            if backtrack(i, j, 1):
                return path
            values[grid[i][j]] = False
