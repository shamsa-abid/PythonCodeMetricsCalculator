def order_by_points(nums):
    return sorted(nums, key=lambda num: sum(int(digit) for digit in str(abs(num))))
