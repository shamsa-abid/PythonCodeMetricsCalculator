def sort_third(l: list):
    sorted_values = sorted([val for idx, val in enumerate(l) if idx % 3 == 0])
    return [val if idx % 3 != 0 else sorted_values.pop(0) for idx, val in enumerate(l)]


# Test cases
print(sort_third([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Output: [2, 6, 3, 4, 8, 9, 5]
