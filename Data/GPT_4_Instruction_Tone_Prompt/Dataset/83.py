def starts_one_ends(n):
    if n == 1:
        return 1
    return 9 * (10 ** (n - 1)) * 2 - (10 ** n)
