
def search(lst):
    lst_count = [(i, lst.count(i)) for i in set(lst)]
    lst_count.sort(key=lambda x: (x[0] < x[1], -x[0]))
    for i, count in lst_count:
        if i <= count:
            return i
    return -1
