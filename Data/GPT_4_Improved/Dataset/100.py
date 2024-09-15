def make_a_pile(n):
    return list(range(n, 2*n+1, 2)) if n % 2 else list(range(n, 2*n+2, 2))
