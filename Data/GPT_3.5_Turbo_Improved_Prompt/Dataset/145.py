def order_by_points(nums):
    def digits_sum(n):
        neg = 1 if n >= 0 else -1
        n = [int(i) for i in str(abs(n))]
        n[0] *= neg
        return sum(n)

    return sorted(nums, key=digits_sum)
