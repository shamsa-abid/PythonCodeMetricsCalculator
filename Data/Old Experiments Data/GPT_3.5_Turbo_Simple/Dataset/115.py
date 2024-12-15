
def max_fill(grid, capacity):
    def calculate_moves(row, remaining_capacity):
        needed_moves = 0
        for well in row:
            if well > 0:
                needed_moves += math.ceil(well / remaining_capacity)
        return needed_moves

    import math

    total_moves = 0
    for row in grid:
        total_moves += calculate_moves(row, capacity)

    return total_moves
