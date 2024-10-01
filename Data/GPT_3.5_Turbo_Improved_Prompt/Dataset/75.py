
from itertools import combinations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_multiply_prime(a):
    primes = [i for i in range(2, 101) if is_prime(i)]
    prime_combinations = combinations(primes, 3)

    for combination in prime_combinations:
        if combination[0] * combination[1] * combination[2] == a:
            return True
    return False
