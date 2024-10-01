def specialFilter(nums):
    count = 0
    for num in nums:
        num = str(abs(num))
        if num[0] in ('1', '3', '5', '7', '9') and num[-1] in ('1', '3', '5', '7', '9'):
            if int(num) > 10:
                count += 1
    return count
