
def make_a_pile(n):
    stones = [n]
    current_stones = n
    for i in range(n - 1):
        if current_stones % 2 == 0:
            current_stones += 1
        else:
            current_stones += 2
        stones.append(current_stones)
    return stones
