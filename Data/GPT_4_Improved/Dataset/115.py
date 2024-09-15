def max_fill(grid, capacity):
    from math import ceil
    return sum(ceil(sum(row) / capacity) for row in grid)
