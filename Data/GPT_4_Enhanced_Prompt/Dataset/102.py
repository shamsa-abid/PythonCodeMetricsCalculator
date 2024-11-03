def choose_num(x, y):
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if y % 2 != 0:
        return y - 1 if y - 1 >= x else -1

    return -1
