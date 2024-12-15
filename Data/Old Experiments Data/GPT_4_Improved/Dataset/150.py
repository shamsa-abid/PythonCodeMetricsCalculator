import math


def x_or_y(n, x, y):
    if n < 2 or any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1)):
        return y
    else:
        return x
