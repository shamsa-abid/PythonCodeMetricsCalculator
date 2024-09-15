def next_smallest(lst):
    lst = list(set(lst))
    if len(lst) > 1:
        lst.sort()
        return (lst[1])
    else:
        return (None)
