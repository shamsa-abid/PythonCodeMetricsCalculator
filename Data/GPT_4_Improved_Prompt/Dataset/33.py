def sort_third(l: list):
    l[::3] = sorted(l[::3])
    return l
