def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = nums[0]
    for i in range(len(nums)):
        temp_sum = 0
        for j in range(i, len(nums)):
            temp_sum += nums[j]
            min_sum = min(min_sum, temp_sum)
    return min_sum
