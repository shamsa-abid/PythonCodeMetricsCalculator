def choose_num(x, y):
    if x > y:
        return -1
    y = y - y % 2
    if y >= x:
        return y
    return -1
