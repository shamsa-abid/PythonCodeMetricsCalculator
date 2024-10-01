def specialFilter(nums):
    def is_odd(num):
        return str(num)[0] in ['1', '3', '5', '7', '9'] and str(num)[-1] in ['1', '3', '5', '7', '9']

    count = 0
    for num in nums:
        if num > 10 and is_odd(num):
            count += 1

    return count
