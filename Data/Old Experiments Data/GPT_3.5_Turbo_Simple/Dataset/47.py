def median(l: list):
    if len(l) == 0:
        return None
    sorted_list = sorted(l)
    n = len(sorted_list)
    if n % 2 == 0:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        return sorted_list[n // 2]
