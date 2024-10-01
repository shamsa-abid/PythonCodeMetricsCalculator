import math
def is_multiply_prime(a):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = math.sqrt(n)
        for i in range(3, int(sqrt_n) + 1, 2):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, int(math.sqrt(a)) + 1):
        while a % i:
            i += 1
        while a % i == 0:
            factors.append(i)
            a /= i
    if a > 1:
        factors.append(a)

    prime_factor_count = sum([1 for v in factors if is_prime(v)])
    return prime_factor_count == 3
