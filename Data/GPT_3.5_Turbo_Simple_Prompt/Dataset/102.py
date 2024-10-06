def choose_num(x, y):
    max_even = -1
    for i in range(x, y+1):
        if i % 2 == 0 and i > max_even:
            max_even = i
    return max_even


# Test Cases
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
