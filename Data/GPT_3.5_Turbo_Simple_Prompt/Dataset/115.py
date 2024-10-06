def max_fill(grid, capacity):
    import math

    def count_buckets_needed(row, capacity):
        total_water = sum(row)
        buckets_needed = math.ceil(total_water / capacity)
        return buckets_needed

    total_buckets = 0
    for row in grid:
        total_buckets += count_buckets_needed(row, capacity)

    return total_buckets


# Example usage
grid1 = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
capacity1 = 1
print(max_fill(grid1, capacity1))  # Output: 6

grid2 = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
capacity2 = 2
print(max_fill(grid2, capacity2))  # Output: 5

grid3 = [[0, 0, 0], [0, 0, 0]]
capacity3 = 5
print(max_fill(grid3, capacity3))  # Output: 0
