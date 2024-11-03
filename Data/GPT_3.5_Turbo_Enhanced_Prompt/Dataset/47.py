def median(l: list):
    l.sort()
    n = len(l)
    mid = n // 2

    if n % 2 == 1:
        return l[mid]
    else:
        return (l[mid - 1] + l[mid]) / 2.0
