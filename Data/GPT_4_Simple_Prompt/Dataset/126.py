def is_sorted(lst):
    # Check if list is sorted in ascending order
    sorted_lst = sorted(lst)
    if lst == sorted_lst:
        # Check for duplicates more than one time
        for i in lst:
            if lst.count(i) > 1:
                return False
        return True
    else:
        return False
