def starts_one_ends(n):
    if n == 1:
        return 1
    return 10 * (10 ** (n - 2)) + 9 * (10 ** (n - 1)) - 9 * (10 ** (n - 2))
