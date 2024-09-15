def make_a_pile(n):
    return [x for x in range(n, 2*n, 2 if n % 2 == 0 else 1)]
