def strange_sort_list(lst):
    sorted_lst = sorted(lst)
    res = [0] * len(lst)

    for i in range(len(lst)):
        if i % 2 == 0:
            res[i] = sorted_lst[i // 2]
        else:
            res[i] = sorted_lst[-((i+1) // 2)]

    return res
