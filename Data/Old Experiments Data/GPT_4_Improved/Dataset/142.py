def sum_squares(lst):
    return sum(n**2 if i % 3 == 0 else n**3 if i % 4 == 0 else n for i, n in enumerate(lst))
