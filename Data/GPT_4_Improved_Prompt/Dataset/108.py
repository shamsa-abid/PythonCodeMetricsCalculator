def count_nums(arr):
    return sum(1 for num in arr if sum(int(digit) for digit in str(abs(num))) * (1 if num >= 0 else -1) > 0)
