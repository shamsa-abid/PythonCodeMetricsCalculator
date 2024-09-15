def next_smallest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()  # Sort the list
    if len(unique_lst) < 2:
        return None
    return unique_lst[1]
