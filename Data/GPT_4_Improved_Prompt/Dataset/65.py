def circular_shift(x, shift):
    s = str(x)
    shift %= len(s)
    return s[-shift:] + s[:-shift]