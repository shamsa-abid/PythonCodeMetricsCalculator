def sort_even(l: list):
    evens = sorted(l[::2])
    l[::2] = evens
    return l
