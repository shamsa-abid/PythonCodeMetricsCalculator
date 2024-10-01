def specialFilter(nums):
    return sum([str(i)[0] in '13579' and str(i)[-1] in '13579' and i > 10 for i in nums])
