import math


def prime_fib(n: int):
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True

    a, b = 0, 1
    while n:
        a, b = b, a + b
        if is_prime(b):
            n -= 1

    return b
