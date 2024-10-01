def closest_integer(value):
    val = float(value)
    if val >= 0:
        if val - int(val) >= 0.5:
            return int(val) + 1
        else:
            return int(val)
    else:
        if -val + int(val) > 0.5:
            return int(val) - 1
        else:
            return int(val)
