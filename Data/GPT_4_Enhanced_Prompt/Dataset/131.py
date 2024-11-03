from operator import mul
from functools import reduce
def digits(n):
    odd_digits = [int(d) for d in str(n) if int(d) % 2 != 0]
    return reduce(mul, odd_digits, 1) if odd_digits else 0
