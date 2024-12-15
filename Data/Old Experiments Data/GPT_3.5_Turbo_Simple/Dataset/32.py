
import math


def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    n = len(xs)

    def f(x):
        return poly(xs, x)

    if n % 2 == 1:
        largest_coeff = max(abs(coeff) for coeff in xs)
        if largest_coeff == 0:
            return 0
        return -math.copysign(1, xs[-1]) * math.pow(largest_coeff / xs[-1], 1/(n-1))

    return 0
