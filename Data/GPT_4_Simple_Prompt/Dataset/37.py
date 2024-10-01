def sort_even(l: list):
    even_indicies = l[::2]
    even_indicies.sort()
    l[::2] = even_indicies
    return l
