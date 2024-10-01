from queue import PriorityQueue
def minPath(grid, k):
    n = len(grid)
    pq = PriorityQueue()
    # To handle all possible movement directions
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    def in_grid(x, y):
        return 0 <= x < n and 0 <= y < n

    def dfs(x, y, k, visited, path):
        if not in_grid(x, y) or visited[x][y] or k == 0:
            if k == 0:
                new_path = path.copy()
                pq.put((new_path, len(new_path)))
            return

        visited[x][y] = True
        path.append(grid[x][y])

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny, k - 1, visited, path)

        visited[x][y] = False
        path.pop()

    for i in range(n):
        for j in range(n):
            visited = [[False] * n for _ in range(n)]
            dfs(i, j, k, visited, [])

    return pq.get()[0]