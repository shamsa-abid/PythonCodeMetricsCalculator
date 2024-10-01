def next_smallest(lst):
    if len(lst) < 2:
        return None

    sorted_lst = sorted(lst)
    second_smallest = sorted_lst[1]

    return second_smallest
