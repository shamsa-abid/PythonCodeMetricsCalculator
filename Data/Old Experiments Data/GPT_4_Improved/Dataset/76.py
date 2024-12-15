import math


def is_simple_power(x, n):
    if n == 1:
        return x == 1
    if n == 0:
        return x == 0

    log_val = math.log(x, n)
    return math.isclose(log_val, round(log_val))
