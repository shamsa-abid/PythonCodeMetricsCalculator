def common(l1: list, l2: list):
    return sorted(list(set(l1) & set(l2)))
