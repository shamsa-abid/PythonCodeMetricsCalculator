def change_base(x: int, base: int):
    digits = []

    while x > 0:
        remainder = x % base
        digits.insert(0, str(remainder))
        x = x // base

    return ''.join(digits)


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
