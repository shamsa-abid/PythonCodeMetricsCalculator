from math import factorial


def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result
