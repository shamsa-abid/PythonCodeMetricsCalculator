
def exchange(lst1, lst2):
    total_odd_lst1 = sum(1 for num in lst1 if num % 2 != 0)
    total_odd_lst2 = sum(1 for num in lst2 if num % 2 != 0)

    if total_odd_lst1 <= total_odd_lst2:
        return "YES"
    else:
        return "NO"
