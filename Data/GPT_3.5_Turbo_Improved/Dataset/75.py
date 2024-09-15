def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, int(a ** 0.33) + 1):
        if not is_prime(i):
            continue
        for j in range(i, int((a / i) ** 0.5) + 1):
            if not is_prime(j):
                continue
            if is_prime(a // (i * j)):
                return True
    return False
