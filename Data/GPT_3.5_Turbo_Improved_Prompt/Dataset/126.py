def is_sorted(lst):
    seen = set()

    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False

        if lst[i] in seen:
            return False
        else:
            seen.add(lst[i])

    return True
