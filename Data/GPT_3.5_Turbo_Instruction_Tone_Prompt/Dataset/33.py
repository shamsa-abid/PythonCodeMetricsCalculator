def sort_third(l):
    indices_to_sort = [i for i in range(len(l)) if i % 3 == 0 and i != 0]
    sorted_values = [l[i] for i in indices_to_sort]

    sorted_values.sort()

    result = l.copy()
    for i, val in zip(indices_to_sort, sorted_values):
        result[i] = val

    return result
