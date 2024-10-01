def max_fill(grid, capacity):
    total_units = sum(sum(row) for row in grid)

    return (total_units + capacity - 1) // capacity
