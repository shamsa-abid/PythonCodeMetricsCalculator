def total_match(lst1, lst2):
    l1, l2 = sum(map(len, lst1)), sum(map(len, lst2))

    return lst1 if l1 <= l2 else lst2
