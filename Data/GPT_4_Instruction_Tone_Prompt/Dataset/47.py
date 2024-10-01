def median(l: list):
    l.sort()
    n = len(l)
    m = n - 1
    if n % 2:
        return l[int((m)/2)]
    else:
        return (l[int((m)/2)] + l[int(m/2 + 1)])/2
