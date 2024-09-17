from fractions import Fraction


def simplify(x, n):
    x_fraction = Fraction(x)
    n_fraction = Fraction(n)
    product = x_fraction * n_fraction
    return product.denominator == 1

print(simplify('1/5', '5/1'))
