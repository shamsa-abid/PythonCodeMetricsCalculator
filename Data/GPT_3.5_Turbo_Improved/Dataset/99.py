from math import floor


def closest_integer(value):
    if '.' in value:
        num = float(value)
        if num % 1 == 0.5:
            return int(num + 0.5 * (num/abs(num)))
        else:
            return round(num)
    else:
        return int(value)


