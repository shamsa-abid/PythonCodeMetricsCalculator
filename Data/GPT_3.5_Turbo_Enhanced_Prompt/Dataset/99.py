from math import floor, ceil


def closest_integer(value):
    if '.' in value:
        num = float(value)
        if num % 1 == 0.5:
            res = ceil(num) if num > 0 else floor(num)
        else:
            res = round(num)
    else:
        res = int(value)

    return res
