def any_int(x, y, z):
    if all(isinstance(i, int) for i in [x, y, z]) and any([x + y == z, y + z == x, z + x == y]):
        return True
    return False
