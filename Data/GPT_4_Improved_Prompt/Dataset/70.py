def strange_sort_list(lst):
    lst = sorted(lst)
    result = []
    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop(-1))
    return result
