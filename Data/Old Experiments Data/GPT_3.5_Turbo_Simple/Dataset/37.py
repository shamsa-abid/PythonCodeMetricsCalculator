def sort_even(l: list):
    even_indices = sorted([x for x in l if l.index(x) % 2 == 0])
    result = l.copy()
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = even_indices.pop(0)
    return result
