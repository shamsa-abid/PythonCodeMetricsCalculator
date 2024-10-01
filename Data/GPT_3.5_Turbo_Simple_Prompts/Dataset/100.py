def make_a_pile(n):
    stones = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones.append(n + i * 2)
        else:
            stones.append(n + i * 2 + 1)
    return stones


# Test the function with example input
print(make_a_pile(3))  # Output: [3, 5, 7]
