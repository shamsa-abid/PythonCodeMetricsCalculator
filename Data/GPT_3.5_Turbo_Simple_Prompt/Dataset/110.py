def exchange(lst1, lst2):
    even_count = 0
    for num in lst1:
        if num % 2 == 0:
            even_count += 1
    for num in lst2:
        if num % 2 == 0:
            even_count -= 1
    if even_count <= 0:
        return "YES"
    else:
        return "NO"
