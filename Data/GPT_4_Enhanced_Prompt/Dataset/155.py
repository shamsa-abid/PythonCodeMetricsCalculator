def even_odd_count(num):
    num_abs_str = str(abs(num))
    evens = sum(1 for digit in num_abs_str if int(digit) % 2 == 0)
    return evens, len(num_abs_str) - evens
