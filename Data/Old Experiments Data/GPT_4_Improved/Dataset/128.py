def prod_signs(arr):
    if not arr:
        return None
    prod_sign = 1
    sum_magnitudes = 0
    for i in arr:
        if i < 0:
            prod_sign *= -1
        elif i == 0:
            return 0
        else:
            sum_magnitudes += i
    return prod_sign * sum_magnitudes
