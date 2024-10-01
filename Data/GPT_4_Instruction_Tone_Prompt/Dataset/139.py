
import math


def special_factorial(n):
    result = 1
    while n > 0:
        result *= math.factorial(n)
        n -= 1
    return result
