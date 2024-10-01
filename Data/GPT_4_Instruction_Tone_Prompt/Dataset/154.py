def cycpattern_check(a, b):
    rotations = [b[i:] + b[:i] for i in range(len(b))]
    return any(rotation in a for rotation in rotations)
