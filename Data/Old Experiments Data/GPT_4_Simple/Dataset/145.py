def order_by_points(nums):
    return sorted(nums, key=lambda num: (sum(int(i) for i in str(abs(num))), nums.index(num)))
