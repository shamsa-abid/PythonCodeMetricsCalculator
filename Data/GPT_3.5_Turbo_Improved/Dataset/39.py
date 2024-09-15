import math


def prime_fib(n: int):
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True

    f = [0, 1]
    while len(f) <= n:
        new_fib = f[-1] + f[-2]
        if is_prime(new_fib):
            f.append(new_fib)

    return f[n]

