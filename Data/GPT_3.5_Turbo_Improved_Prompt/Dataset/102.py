def choose_num(x, y):
    if x >= y or x % 2 != 0:
        return -1
    return y - (1 if y % 2 != 0 else 0)
