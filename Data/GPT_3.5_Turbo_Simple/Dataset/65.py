def circular_shift(x, shift):
    x_str = str(x)
    shift = shift % len(x_str)
    if shift == 0:
        return x_str
    else:
        shifted = x_str[-shift:] + x_str[:-shift]
        return shifted[::-1] if shift > len(x_str) else shifted.strip("0") if shifted != "0" else "0"
