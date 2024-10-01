def strange_sort_list(lst):
    sorted_lst = []
    lst.sort()
    while lst:
        sorted_lst.append(lst.pop(0))
        if lst:
            sorted_lst.append(lst.pop())
    return sorted_lst


# Test cases
print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([]))  # []
