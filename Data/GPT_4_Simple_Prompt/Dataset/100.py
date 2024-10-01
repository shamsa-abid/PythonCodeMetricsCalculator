def make_a_pile(n):
    if n <= 0:
        return []
    return [i for i in range(n, 2*n, 2 if n % 2 == 0 else 1)]