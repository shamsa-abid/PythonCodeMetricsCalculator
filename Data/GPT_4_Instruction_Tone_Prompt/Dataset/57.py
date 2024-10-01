def monotonic(l: list):
    if len(l) <= 2:
        return True
    if all(l[i] <= l[i + 1] for i in range(len(l) - 1)):
        return True
    if all(l[i] >= l[i + 1] for i in range(len(l) - 1)):
        return True
    return False
