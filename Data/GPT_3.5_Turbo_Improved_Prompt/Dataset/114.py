def minSubArraySum(nums):
    max_sum = float('-inf')
    min_sum = float('inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        min_sum = min(min_sum, current_sum)

    return min_sum if max_sum >= 0 else max(nums)
