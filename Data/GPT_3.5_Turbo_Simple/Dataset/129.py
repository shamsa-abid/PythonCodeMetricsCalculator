
def minPath(grid, k):
    def get_neighbors(grid, visited, x, y):
        n = len(grid)
        neighbors = []
        if x > 0 and not visited[x-1][y]:
            neighbors.append((x-1, y))
        if x < n-1 and not visited[x+1][y]:
            neighbors.append((x+1, y))
        if y > 0 and not visited[x][y-1]:
            neighbors.append((x, y-1))
        if y < n-1 and not visited[x][y+1]:
            neighbors.append((x, y+1))
        return neighbors

    n = len(grid)
    visited = [[False for _ in range(n)] for _ in range(n)]
    path = []

    def dfs(x, y, remaining):
        if remaining == 0:
            return True

        visited[x][y] = True
        path.append(grid[x][y])

        for nx, ny in get_neighbors(grid, visited, x, y):
            if dfs(nx, ny, remaining - 1):
                return True

        visited[x][y] = False
        path.pop()
        return False

    for i in range(n):
        for j in range(n):
            if dfs(i, j, k - 1):
                return path
