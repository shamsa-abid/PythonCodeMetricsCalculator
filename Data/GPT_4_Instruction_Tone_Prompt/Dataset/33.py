def sort_third(l: list) -> list:
    thrid_elements = sorted([l[i] for i in range(0, len(l), 3)])
    j = 0
    for i in range(0, len(l), 3):
        l[i] = thrid_elements[j]
        j += 1
    return l
