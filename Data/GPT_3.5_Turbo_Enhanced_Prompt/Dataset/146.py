def specialFilter(nums):
    odd_digits = set([1, 3, 5, 7, 9])
    count = 0

    for num in nums:
        if num > 10:
            first_digit = int(str(num)[0])
            last_digit = int(str(num)[-1])

            if first_digit in odd_digits and last_digit in odd_digits:
                count += 1

    return count
