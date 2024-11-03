
def minPath(grid, k):
    n = len(grid)
    val = min(min(row) for row in grid)

    ans = []
    for i in range(k):
        ans.append(1) if i % 2 == 0 else ans.append(val)

    return ans
