def is_equal_to_sum_even(n):
    count_even = 0
    for i in range(2, n + 1, 2):
        if n - i >= 0:
            count_even += 1
            if count_even == 4:
                return True
    return False


# Test cases
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
