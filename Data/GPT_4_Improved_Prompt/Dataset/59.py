import math


def largest_prime_factor(n: int) -> int:
    max_prime = -1

    while n % 2 == 0:
        max_prime = 2
        n >>= 1

    while n % 3 == 0:
        max_prime = 3
        n = n // 3

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        while n % i == 0:
            max_prime = i
            n = n // i
        while n % (i + 2) == 0:
            max_prime = i + 2
            n = n // (i + 2)

    if n > 4:
        max_prime = n

    return max_prime
