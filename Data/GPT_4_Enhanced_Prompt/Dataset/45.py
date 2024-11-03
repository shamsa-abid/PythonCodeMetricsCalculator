def triangle_area(a, h):
    if isinstance(a, (int, float)) and isinstance(h, (int, float)):
        if a > 0 and h > 0:
            return a * h / 2.0
        else:
            raise ValueError(
                'Both base and height must be nonnegative real numbers')
    else:
        raise TypeError('Both base and height must be real numbers')
