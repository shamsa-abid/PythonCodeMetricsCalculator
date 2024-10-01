from fractions import Fraction
def simplify(x, n):
    # convert string fractions to Fraction objects
    x_frac, n_frac = Fraction(x), Fraction(n)
    # multiply fractions and check if result is integer (denominator is 1)
    return (x_frac * n_frac).denominator == 1
