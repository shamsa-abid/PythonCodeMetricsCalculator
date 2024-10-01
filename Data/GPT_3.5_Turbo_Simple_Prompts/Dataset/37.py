def sort_even(l: list):
    even_values = sorted([x for x in l[::2]])
    result = [0] * len(l)
    result[::2] = even_values
    result[1::2] = l[1::2]

    return result


# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
