def unique_digits(x):
    la = []
    for i in x:
        if all(int(j) % 2 != 0 for j in str(i)):
            la.append(i)
    return sorted(la)
