def minSubArraySum(nums):
    current_sum = float('inf')
    total_sum = 0
    for num in nums:
        total_sum += num
        current_sum = min(total_sum, current_sum, num)
        if total_sum > 0:
            total_sum = 0
    return current_sum
