def change_base(x: int, base: int) -> str:
    number = ""
    while x > 0:
        number = str(x % base) + number
        x = x // base
    return number
