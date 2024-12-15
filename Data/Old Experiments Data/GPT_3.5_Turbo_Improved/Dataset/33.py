def sort_third(l: list):
    l_copy = list(l)
    l_copy[::3] = sorted(l_copy[::3])
    return l_copy
