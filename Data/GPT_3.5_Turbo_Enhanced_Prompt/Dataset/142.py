
def sum_squares(lst):
    result = [x**2 if i % 3 == 0 else x**3 if i %
              4 == 0 and i % 3 != 0 else x for i, x in enumerate(lst)]
    return sum(result)
