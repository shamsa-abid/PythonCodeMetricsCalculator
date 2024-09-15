def is_simple_power(x, n):
    if x == 1 or n == 1:
        return x == 1
    power = n
    while power < x:
        power *= n
    return power == x
