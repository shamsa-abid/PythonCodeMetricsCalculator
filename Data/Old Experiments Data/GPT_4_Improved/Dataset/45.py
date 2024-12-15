def triangle_area(a, h):
    if isinstance(a, (int, float)) and isinstance(h, (int, float)):
        if a > 0 and h > 0:
            return a * h / 2.0
        else:
            raise ValueError(
                "Length of a side and height must be greater than 0.")
    else:
        raise TypeError("Length of a side and height must be a number.")
