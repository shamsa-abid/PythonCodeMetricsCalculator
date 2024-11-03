import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def prime_fib(n: int):
    fib_seq = [0, 1]
    while n > 0:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        if is_prime(fib_seq[-1]):
            n -= 1
    return fib_seq[-2]
