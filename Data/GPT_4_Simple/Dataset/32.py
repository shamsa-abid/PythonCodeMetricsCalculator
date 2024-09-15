import math
import numpy as np


def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    roots = np.roots(xs[::-1])
    real_roots = [root.real for root in roots if root.imag == 0]
    return min(real_roots, key=abs)
