def choose_num(x, y):
    if x > y or x % 2 == 1:
        return -1
    else:
        return y if y % 2 == 0 else y - 1
