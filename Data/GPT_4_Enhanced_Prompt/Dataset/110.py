def exchange(lst1, lst2):
    odd = sum(1 for i in lst1 if i % 2)
    even = sum(1 for i in lst2 if i % 2 == 0)
    return "YES" if even >= odd else "NO"
