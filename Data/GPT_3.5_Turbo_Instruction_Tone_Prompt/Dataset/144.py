
from fractions import Fraction


def simplify(x, n):
    result = Fraction(x) * Fraction(n)
    return result.denominator == 1
