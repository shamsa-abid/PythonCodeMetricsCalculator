def exchange(lst1, lst2):
    count_odd_lst1 = sum(1 for i in lst1 if i % 2 != 0)
    count_even_lst2 = sum(1 for i in lst2 if i % 2 == 0)

    if count_even_lst2 >= count_odd_lst1:
        return "YES"
    else:
        return "NO"
