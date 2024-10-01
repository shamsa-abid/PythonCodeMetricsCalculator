def max_fill(grid, capacity):
    import math

    # Total amount of water in the wells
    total_water = sum(sum(row) for row in grid)

    # Number of times to lower the buckets equals to ceiling division of the total amount of water by the capacity of the bucket
    return math.ceil(total_water / capacity)
