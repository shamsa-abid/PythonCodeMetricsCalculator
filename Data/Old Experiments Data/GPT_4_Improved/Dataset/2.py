def truncate_number(number: float) -> float:
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a floating point number")

    if number < 0:
        raise ValueError("Input must be a positive number")

    return number - int(number)
