def total_match(lst1, lst2):
    len_lst1 = sum(len(word) for word in lst1)
    len_lst2 = sum(len(word) for word in lst2)
    if len_lst1 <= len_lst2:
        return lst1
    else:
        return lst2