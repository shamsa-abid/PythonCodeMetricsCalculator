
def sorted_list_sum(lst):
    new_lst = [i for i in lst if len(i) % 2 == 0]
    return sorted(new_lst, key=lambda x: (len(x), x))
