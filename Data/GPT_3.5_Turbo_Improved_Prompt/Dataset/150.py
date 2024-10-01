def x_or_y(n, x, y):
    import math

    if n == 1:
        return y
    if n == 2:
        return x

    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return y

    return x
