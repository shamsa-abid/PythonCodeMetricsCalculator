import math


def sum_squares(lst):
    return sum(int(math.ceil(num))**2 for num in lst)
