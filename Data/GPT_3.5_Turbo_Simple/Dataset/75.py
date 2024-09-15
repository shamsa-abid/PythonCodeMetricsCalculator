def is_multiply_prime(a):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors(num):
        factors = []
        for i in range(2, num+1):
            if num % i == 0 and is_prime(i):
                factors.append(i)
                num = num // i
        return factors

    factors = prime_factors(a)
    return len(factors) == 3 and a == factors[0] * factors[1] * factors[2]
