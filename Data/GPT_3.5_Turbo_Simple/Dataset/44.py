def change_base(x: int, base: int):
    def convert(num, base):
        if num == 0:
            return ""
        return convert(num // base, base) + str(num % base)

    if x == 0:
        return "0"
    return convert(x, base) if x > 0 else "-" + convert(-x, base) if x < 0 else ""


METADATA = {}
