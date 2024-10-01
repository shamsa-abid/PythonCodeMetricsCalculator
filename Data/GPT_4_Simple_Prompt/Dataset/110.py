def exchange(lst1, lst2):
    odd_nums_lst1 = [num for num in lst1 if num % 2 != 0]
    even_nums_lst2 = [num for num in lst2 if num % 2 == 0]

    return "YES" if len(odd_nums_lst1) <= len(even_nums_lst2) else "NO"
