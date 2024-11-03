import math


def is_simple_power(x, n):
    if n == 1:
        return x == 1
    elif x == 1:
        return True
    else:
        result = math.log(x, n)
        return result.is_integer()
