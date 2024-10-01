def next_smallest(lst):
    try:
        lst = sorted(set(lst))
        return lst[1] if len(lst) > 1 else None
    except (TypeError, ValueError):
        return None
