def max_fill(grid, capacity):
    total_fill = 0

    for row in grid:
        total_fill += sum(row)

    buckets_needed = total_fill // capacity
    if total_fill % capacity != 0:
        buckets_needed += 1

    return buckets_needed
