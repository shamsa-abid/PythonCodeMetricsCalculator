import math
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # initialize the largest prime
    max_prime = -1

    # while n is even, divide it
    while n % 2 == 0:
        max_prime = 2
        n >>= 1   # equivalent to n /= 2

    # checking for factors upto square root of a number
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n / i

    # when number is greater than 2
    if n > 2:
        max_prime = n

    return int(max_prime)
