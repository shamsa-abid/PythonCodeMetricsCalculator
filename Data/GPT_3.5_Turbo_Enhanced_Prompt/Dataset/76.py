def is_simple_power(x, n):
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        if x % n != 0:
            return False
        return is_simple_power(x / n, n)
