def starts_one_ends(n):
    if n == 1:
        return 1
    else:
        return 10 * (10 ** (n - 2)) + 8 * (10 ** (n - 1))
