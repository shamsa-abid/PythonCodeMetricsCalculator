import scipy.optimize as opt


def find_zero(xs: list):
    return opt.newton(lambda x: poly(xs, x), 0)
