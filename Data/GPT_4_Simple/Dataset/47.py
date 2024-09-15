def median(l: list):
    l.sort()
    length = len(l)
    index = length // 2

    if length % 2:
        return l[index]
    else:
        return (l[index - 1] + l[index]) / 2
