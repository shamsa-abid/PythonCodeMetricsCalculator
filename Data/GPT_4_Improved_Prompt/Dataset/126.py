from collections import Counter


def is_sorted(lst):
    counts = Counter(lst)
    if any(value > 2 for value in counts.values()):
        return False
    return lst == sorted(lst)
