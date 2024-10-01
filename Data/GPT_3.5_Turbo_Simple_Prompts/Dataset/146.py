def specialFilter(nums):
    def is_odd_digit(num):
        first_digit = abs(num) // 10**(len(str(abs(num)))-1)
        last_digit = abs(num) % 10
        if first_digit in [1, 3, 5, 7, 9] and last_digit in [1, 3, 5, 7, 9]:
            return True
        return False

    count = 0
    for num in nums:
        if num > 10 and is_odd_digit(num):
            count += 1

    return count


# Test cases
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2
