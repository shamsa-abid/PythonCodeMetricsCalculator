def minSubArraySum(nums):
    max_sum = float('-inf')
    min_sum = float('inf')
    curr_sum = 0

    for num in nums:
        curr_sum += num
        max_sum = max(max_sum, curr_sum - min_sum)
        min_sum = min(min_sum, curr_sum)

    return max_sum if max_sum != float('-inf') else max(nums) * -1
