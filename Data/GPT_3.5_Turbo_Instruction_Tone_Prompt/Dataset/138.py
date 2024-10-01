def is_equal_to_sum_even(n):
    if n % 2 != 0:  # If n is not even, it cannot be written as the sum of even numbers
        return False

    count = 0
    for i in range(2, n // 2 + 1, 2):  # Check possible even numbers
        if count == 4:
            return True
        if n - i >= 0:
            count += 1

    if count == 4:  # Check if 4 even numbers were found
        return True
    else:
        return False
