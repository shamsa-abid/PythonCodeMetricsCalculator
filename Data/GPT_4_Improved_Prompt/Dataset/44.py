def change_base(x: int, base: int) -> str:
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    return ''.join(digits[::-1])
