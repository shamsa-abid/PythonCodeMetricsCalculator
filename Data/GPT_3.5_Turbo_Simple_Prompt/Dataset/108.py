def count_nums(arr):
    def sum_of_digits(num):
        if num == 0:
            return 0
        elif num < 0:
            return -sum(int(digit) for digit in str(num) if digit.isdigit())
        else:
            return sum(int(digit) for digit in str(num) if digit.isdigit())

    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1

    return count


# Test cases
print(count_nums([]))  # Output: 0
print(count_nums([-1, 11, -11]))  # Output: 1
print(count_nums([1, 1, 2]))  # Output: 3
