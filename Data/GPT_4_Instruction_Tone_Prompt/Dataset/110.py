def exchange(lst1, lst2):
    if sum(1 for i in lst1 if i % 2 != 0) <= sum(1 for i in lst2 if i % 2 == 0):
        return "YES"
    else:
        return "NO"
