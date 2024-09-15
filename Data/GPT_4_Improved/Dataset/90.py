def next_smallest(lst):
    try:
        sorted_lst = sorted(set(lst))
        return sorted_lst[1] if len(sorted_lst) > 1 else None
    except TypeError:
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
