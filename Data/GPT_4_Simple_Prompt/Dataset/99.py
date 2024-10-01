def closest_integer(value):
    float_val = float(value)
    if float_val >= 0:
        return int(round(float_val))
    else:
        return -int(round(abs(float_val)))
