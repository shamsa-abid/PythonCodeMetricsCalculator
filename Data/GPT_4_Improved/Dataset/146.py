def specialFilter(nums):
    count = 0
    odd_digits = set('13579')
    for num in nums:
        if num > 10:
            s_num = str(num)
            if (s_num[0] in odd_digits) and (s_num[-1] in odd_digits):
                count += 1
    return count
