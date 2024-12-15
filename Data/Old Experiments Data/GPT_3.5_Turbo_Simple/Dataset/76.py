def is_simple_power(x, n):
    if x == 1:
        return True
    if x == n:
        return True
    if n == 1:
        return False
    if n == 0:
        if x == 0:
            return True
        return False
    if n == 3:
        if x == 3:
            return False
    if n == 2:
        if x == 2:
            return True
    if x % n != 0:
        return False
    while x % n == 0:
        x = x // n
        if x == 1:
            return True
    return False
