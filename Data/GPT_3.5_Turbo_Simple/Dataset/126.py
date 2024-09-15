def is_sorted(lst):
    # Check for duplicates
    for num in lst:
        if lst.count(num) > 1:
            return False

    # Check if list is sorted
    sorted_lst = sorted(lst)
    if lst == sorted_lst:
        return True
    else:
        return False
