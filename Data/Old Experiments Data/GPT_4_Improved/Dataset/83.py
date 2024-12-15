def starts_one_ends(n):
    if n > 1:
        return 18 * (10 ** (n - 2))
    else:
        return 1 if n == 1 else 0
