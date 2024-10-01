def strange_sort_list(lst):
    if not lst:
        return []

    lst.sort()
    result = []
    left, right = 0, len(lst) - 1
    while left <= right:
        if left == right:
            result.append(lst[left])
        else:
            result.append(lst[left])
            result.append(lst[right])
        left += 1
        right -= 1

    return result
