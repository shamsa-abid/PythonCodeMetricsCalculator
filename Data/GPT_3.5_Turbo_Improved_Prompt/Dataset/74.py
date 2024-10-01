def total_match(lst1, lst2):
    total_chars_lst1 = sum(len(st) for st in lst1)
    total_chars_lst2 = sum(len(st) for st in lst2)

    return lst1 if total_chars_lst1 <= total_chars_lst2 else lst2
