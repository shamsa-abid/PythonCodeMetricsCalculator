def next_smallest(lst):
    if len(set(lst)) < 2:
        return None
    return sorted(set(lst))[1]
