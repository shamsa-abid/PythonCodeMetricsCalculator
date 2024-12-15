def is_sorted(lst):
    if lst == sorted(lst) and len(lst) == len(set(lst)):
        return True
    else:
        return False
