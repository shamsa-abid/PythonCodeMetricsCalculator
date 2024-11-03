def sort_third(l: list):
    sort_idx = list(range(0, len(l), 3))
    sorted_values = [val for idx, val in sorted(
        zip(sort_idx, [l[i] for i in sort_idx]))]

    result = l.copy()
    for idx, val in zip(sort_idx, sorted_values):
        result[idx] = val

    return result
