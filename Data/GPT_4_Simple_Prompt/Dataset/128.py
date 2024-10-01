def prod_signs(arr):
    if not arr:
        return None

    zero_present = 0 in arr
    negative_count = sum(1 for num in arr if num < 0)
    magnitude_sum = sum(abs(num) for num in arr)

    if zero_present:
        return 0
    if negative_count % 2 == 0:
        return magnitude_sum
    else:
        return -magnitude_sum
