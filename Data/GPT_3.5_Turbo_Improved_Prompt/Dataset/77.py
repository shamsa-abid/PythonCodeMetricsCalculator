
def iscube(a):
    import math
    a = abs(a)
    return int(round(math.pow(a, 1/3)) ** 3) == a
