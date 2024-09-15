def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 'One of the supplied number is 0.'
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
