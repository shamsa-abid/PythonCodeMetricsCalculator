def is_equal_to_sum_even(n):
    if n % 4 == 0:
        return True
    elif n % 2 == 0 and (n-2) % 4 == 0:
        return True
    else:
        return False
