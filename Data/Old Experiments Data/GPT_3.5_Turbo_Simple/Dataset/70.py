def strange_sort_list(lst):
    odd = sorted(lst)
    even = sorted(lst, reverse=True)
    result = []

    while odd or even:
        if odd:
            result.append(odd.pop(0))
        if even:
            result.append(even.pop(0))

    return result
