def max_fill(grid, capacity):
    return sum([(-sum(r)) // -capacity for r in grid])
