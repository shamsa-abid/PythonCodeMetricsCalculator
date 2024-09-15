def sum_squares(lst):
    new_lst = [i**2 if idx % 3 ==
               0 else (i**3 if idx % 4 == 0 else i) for idx, i in enumerate(lst)]
    return sum(new_lst)
