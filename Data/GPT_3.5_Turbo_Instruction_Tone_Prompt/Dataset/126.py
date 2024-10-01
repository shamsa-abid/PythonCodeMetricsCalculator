def is_sorted(lst):
    if lst == sorted(set(lst)):
        return True
    else:
        return False
