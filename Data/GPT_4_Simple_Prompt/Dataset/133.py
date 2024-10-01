import math
def sum_squares(lst):
    return sum(math.ceil(number)**2 for number in lst)
