def minSubArraySum(nums):
    current_min = float('inf')
    current_sum = 0
    for num in nums:
        if current_sum > 0:
            current_sum = num
        else:
            current_sum += num
        current_min = min(current_min, current_sum)
    return current_min if current_min != float('inf') else 0
