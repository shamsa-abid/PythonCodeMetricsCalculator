def count_up_to(n):
    primes = [True]*(n+1)
    p = 2
    while p**2 <= n:
        if primes[p] is True:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    result = [p for p in range(2, n) if primes[p]]
    return result