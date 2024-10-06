def order_by_points(nums):
    # Define a custom key function to sort numbers by the sum of their digits
    def digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    # Sort the list of numbers using the custom key function and the original index as secondary key
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
