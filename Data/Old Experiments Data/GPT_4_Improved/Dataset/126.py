from collections import Counter


def is_sorted(lst):
    if lst != sorted(lst):
        return False
    count = Counter(lst)
    if any(value > 2 for value in count.values()):
        return False
    return True
