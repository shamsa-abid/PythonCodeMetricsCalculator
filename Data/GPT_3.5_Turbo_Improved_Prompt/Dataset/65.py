def circular_shift(x, shift):
    s = str(x)

    # Calculate the effective shift value
    shift %= len(s)

    # Perform circular shift based on the effective shift value
    result = s[-shift:] + s[:-shift]

    return result
