import math
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True


def x_or_y(n, x, y):
    return x if is_prime(n) else y
