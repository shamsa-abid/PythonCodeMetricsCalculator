def unique_digits(x):
    return sorted([i for i in x if all(int(c) % 2 == 1 for c in str(i))])
