def circular_shift(x, shift):
    x = str(x)
    digits = len(x)
    x = x.zfill(digits)
    if shift > digits:
        return x[::-1]
    else:
        return x[-shift:] + x[:-shift]
