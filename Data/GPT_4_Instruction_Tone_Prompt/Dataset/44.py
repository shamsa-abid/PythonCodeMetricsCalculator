def change_base(x: int, base: int) -> str:
    if isinstance(x, int) and isinstance(base, int) and (base < 10):
        return str(int(str(x), base))
    else:
        raise ValueError("Invalid Input")
