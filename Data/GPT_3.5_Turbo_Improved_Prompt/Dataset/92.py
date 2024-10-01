def any_int(x, y, z):
    if all(isinstance(i, int) for i in [x, y, z]):
        return any(i == j + k for i, j, k in [(x, y, z), (y, x, z), (z, x, y)])
    return False
