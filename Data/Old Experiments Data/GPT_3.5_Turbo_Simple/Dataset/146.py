def specialFilter(nums):
    def is_odd(num):
        return num % 2 != 0

    def has_odd_first_and_last_digit(num):
        num_str = str(abs(num))
        return is_odd(int(num_str[0])) and is_odd(int(num_str[-1]))

    count = 0
    for num in nums:
        if num > 10 and has_odd_first_and_last_digit(num):
            count += 1

    return count
