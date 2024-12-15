def is_equal_to_sum_even(n):
    if isinstance(n, int) and n >= 0:
        return n % 2 == 0 and n >= 8
    else:
        raise ValueError("Input should be a non-negative integer")
