import scipy.optimize
def find_zero(xs: list):
    return scipy.optimize.newton(poly.bind(None, xs), 0)
