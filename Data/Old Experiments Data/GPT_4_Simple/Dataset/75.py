def is_multiply_prime(a):
    def is_prime(n):
        if n != int(n) or n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n ** 0.5)
        for d in range(3, 1 + max_divisor, 2):
            if n % d == 0:
                return False
        return True

    factors = []
    for i in range(2, a + 1):
        while a % i == 0:
            factors.append(i)
            a = a / i
        if a == 1:
            break

    if len(factors) != 3:
        return False
    else:
        for factor in factors:
            if not is_prime(factor):
                return False
    return True
