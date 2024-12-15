def strange_sort_list(lst):
    lst.sort()
    start_lst = lst[::2]
    end_lst = lst[1::2][::-1]
    return [el for pair in zip(start_lst, end_lst) for el in pair] + start_lst[len(end_lst):]
