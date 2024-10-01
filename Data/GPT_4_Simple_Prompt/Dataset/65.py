def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    # Convert the integer into a string format
    x = str(x)
    # Find the length of the string
    length = len(x)

    # If the shift is greater than the number of digits, reverse the string.
    if shift > length:
        return x[::-1]
    # Perform the circular shift
    else:
        return x[-shift:] + x[:-shift]
