def is_simple_power(x, n):
    num = 0
    while n**num <= x:
        if n**num == x:
            return True
        num += 1
    return False
