def starts_one_ends(n):
    count = 9 * 10 ** (n - 1)  # Count of numbers that start with 1
    count += 9 * 10 ** (n - 1)  # Count of numbers that end with 1
    count -= 1  # Remove double count of numbers that start and end with 1
    return count
