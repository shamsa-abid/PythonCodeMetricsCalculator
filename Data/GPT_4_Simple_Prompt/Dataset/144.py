from fractions import Fraction
def simplify(x, n):
    x = Fraction(x)
    n = Fraction(n)
    result = x * n
    # if the result is an integer
    if result.denominator == 1:
        return True
    else:
        return False
