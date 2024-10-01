def strange_sort_list(lst):
    lst.sort()
    start, end = 0, len(lst) - 1
    sorted_list = []
    while start <= end:
        if start == end:
            sorted_list.append(lst[start])
            break
        sorted_list.append(lst[start])
        sorted_list.append(lst[end])
        start += 1
        end -= 1
    return sorted_list
