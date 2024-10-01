def sort_even(l: list):
    even_indices = [num for i, num in enumerate(l) if i % 2 == 0]
    even_indices.sort()
    for i in range(0, len(l), 2):
        l[i] = even_indices.pop(0)
    return l
