def incr_list(l: list):
    return [e + 1 for e in l] if l else []


# Test cases
print(incr_list([]))  # []
print(incr_list([3, 2, 1]))  # [4, 3, 2]
# [6, 3, 6, 3, 4, 4, 10, 1, 124]
print(incr_list([5, 2, 5, 2, 3, 3, 9, 0, 123]))
