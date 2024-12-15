def double_the_difference(lst):
    return sum(i**2 for i in lst if type(i) == int and i > 0 and i % 2 != 0)
