def specialFilter(nums):
    count = 0
    odd_digits = (1, 3, 5, 7, 9)

    for num in nums:
        if num > 10 and str(num)[0] in map(str, odd_digits) and str(num)[-1] in map(str, odd_digits):
            count += 1

    return count
