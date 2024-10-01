def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # If the number is less than 8 (the smallest sum of 4 positive even numbers), it can't be written as the sum
    if n < 8:
        return False

    # If the number is greater or equal to 8, then it must also be even, since the sum of even numbers is always even
    elif n % 2 != 0:
        return False

    # If the number is even and greater or equal to 8, then it can be written as the sum of 4 positive even numbers
    else:
        return True
