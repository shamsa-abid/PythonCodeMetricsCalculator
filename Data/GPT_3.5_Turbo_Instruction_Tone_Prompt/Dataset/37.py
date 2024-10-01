def sort_even(l):
    even_indices = sorted([val for idx, val in enumerate(l) if idx % 2 == 0])
    result = [val if idx % 2 != 0 else even_indices.pop(
        0) for idx, val in enumerate(l)]
    return result
