def sorted_list_sum(lst):
    # Deleting strings with odd lengths
    filtered_lst = [s for s in lst if len(s) % 2 == 0]
    # Sorting the list: first by length, then alphabetically
    sorted_lst = sorted(filtered_lst, key=lambda x: (len(x), x))
    return sorted_lst