def get_row(lst, x):
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if x in lst[i]]
    return sorted(coords, key=lambda x: (x[0], -x[1]))
