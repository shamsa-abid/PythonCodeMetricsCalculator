def sum_squares(lst):
    total = 0
    for num in lst:
        total += (int(num) + (num > int(num))) ** 2
    return total


# Test cases
print(sum_squares([1, 2, 3]))  # 14
print(sum_squares([1, 4, 9]))  # 98
print(sum_squares([1, 3, 5, 7]))  # 84
print(sum_squares([1.4, 4.2, 0]))  # 29
print(sum_squares([-2.4, 1, 1]))  # 6
