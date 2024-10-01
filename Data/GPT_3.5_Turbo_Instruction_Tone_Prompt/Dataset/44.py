def change_base(x: int, base: int):
    if x == 0:
        return "0"

    digits = []
    while x > 0:
        remainder = x % base
        digits.insert(0, str(remainder))
        x //= base

    return "".join(digits)
