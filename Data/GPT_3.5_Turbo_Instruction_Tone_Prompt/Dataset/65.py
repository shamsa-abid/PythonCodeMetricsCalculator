def circular_shift(x, shift):
    x_str = str(x)
    shift %= len(x_str)  # Ensure shift is within the range of digits

    if shift == 0:
        return x_str
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]
        return shifted_str
