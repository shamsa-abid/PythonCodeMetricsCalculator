from heapq import heappop, heappush
def min_path(grid: list[list[int]], k: int) -> list[int]:
    n = len(grid)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start = min((i, j) for i in range(n) for j in range(n) if grid[i][j] == 1)
    heap = [(grid[start[0]][start[1]], start, [grid[start[0]][start[1]]])]

    while heap:
        val, (x, y), path = heappop(heap)
        if len(path) == k:
            return path
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                heappush(
                    heap, (max(val, grid[nx][ny]), (nx, ny), path + [grid[nx][ny]]))
