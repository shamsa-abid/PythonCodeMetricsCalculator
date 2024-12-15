def sorted_list_sum(lst):
    even_lst = [item for item in lst if len(item) % 2 == 0]
    even_lst.sort()
    return sorted(even_lst, key=len)
