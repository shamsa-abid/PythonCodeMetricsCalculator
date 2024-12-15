def iscube(a):
    a = abs(a)
    cubic_root = round(a ** (1/3))
    return cubic_root ** 3 == a
