def prod_signs(arr):
    if not arr:
        return None

    prod, abs_sum = 1, 0

    for num in arr:
        sign = (1 if num > 0 else -1 if num < 0 else 0)
        prod *= sign
        abs_sum += abs(num)

    return prod * abs_sum if prod != 0 else 0
