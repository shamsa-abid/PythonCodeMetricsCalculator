def strange_sort_list(lst):
    res, switch = [], True
    sorted_lst = sorted(lst)

    while sorted_lst:
        res.append(sorted_lst.pop(0) if switch else sorted_lst.pop())
        switch = not switch

    return res
