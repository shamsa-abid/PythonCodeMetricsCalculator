import math
def closest_integer(value):
    num = float(value)
    if num >= 0:
        return math.ceil(num) if num - math.floor(num) >= 0.5 else math.floor(num)
    else:
        return math.floor(num) if math.ceil(num) - num >= 0.5 else math.ceil(num)
