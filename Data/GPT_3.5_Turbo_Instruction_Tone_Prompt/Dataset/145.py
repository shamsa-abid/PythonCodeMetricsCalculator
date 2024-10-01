def order_by_points(nums):
    def calculate_sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    return sorted(nums, key=lambda x: (calculate_sum_of_digits(x), nums.index(x)))
