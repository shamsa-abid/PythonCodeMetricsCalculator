def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    factors = []
    d = 2
    while d * d <= a:
        while (a % d) == 0:
            factors.append(d)
            a //= d
        d += 1
    if a > 1:
        factors.append(a)

    if len(factors) != 3:
        return False
    for factor in factors:
        if not is_prime(factor):
            return False
    return True