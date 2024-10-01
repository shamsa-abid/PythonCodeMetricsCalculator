def sum_squares(lst):
    return sum(num ** 2 if idx % 3 == 0 else num ** 3 if idx % 4 == 0 else num for idx, num in enumerate(lst))
