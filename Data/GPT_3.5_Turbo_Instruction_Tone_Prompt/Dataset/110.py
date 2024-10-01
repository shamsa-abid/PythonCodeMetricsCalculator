def exchange(lst1, lst2):
    for num in lst1:
        if num % 2 != 0:
            for i in range(len(lst2)):
                if lst2[i] % 2 == 0:
                    lst1[lst1.index(num)] = lst2[i]
                    break
            else:
                return "NO"
    return "YES"
