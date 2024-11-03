def any_int(x, y, z):
    return all(map(lambda v: isinstance(v, int), [x, y, z])) and any([x + y == z, x + z == y, y + z == x])
