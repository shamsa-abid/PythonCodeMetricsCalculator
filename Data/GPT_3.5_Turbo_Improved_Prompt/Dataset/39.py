
import math


def is_prime(p):
    if p < 2:
        return False
    for k in range(2, int(math.sqrt(p)) + 1):
        if p % k == 0:
            return False
    return True


def prime_fib(n: int):
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        if is_prime(next_fib):
            n -= 1
        if n == 0:
            return next_fib
