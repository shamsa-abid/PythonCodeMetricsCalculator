def next_smallest(lst):
    if len(set(lst)) < 2:
        return None
    else:
        lst.sort()
        lst_without_duplicates = list(dict.fromkeys(lst))
        return lst_without_duplicates[1]
