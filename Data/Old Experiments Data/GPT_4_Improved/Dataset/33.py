def sort_third(l: list):
    sorted_indices = sorted(l[::3])
    l[::3] = sorted_indices
    return l
