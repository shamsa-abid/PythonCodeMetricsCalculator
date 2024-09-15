def fibfib(n: int):
    if n < 3:
        return max(0, n - 2)

    a, b, c = 0, 0, 1
    for _ in range(n - 2):
        a, b, c = b, c, a + b + c
    return c
