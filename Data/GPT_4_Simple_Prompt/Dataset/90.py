def next_smallest(lst):
    sorted_unique_list = sorted(set(lst))
    if len(sorted_unique_list) > 1:
        return sorted_unique_list[1]
    else:
        return None
