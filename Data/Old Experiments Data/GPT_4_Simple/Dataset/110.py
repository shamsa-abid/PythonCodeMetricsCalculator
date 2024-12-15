def exchange(lst1, lst2):
    odd_lst1 = [i for i in lst1 if i % 2 != 0]
    even_lst2 = [i for i in lst2 if i % 2 == 0]

    if len(odd_lst1) <= len(even_lst2):
        return "YES"
    else:
        return "NO"
