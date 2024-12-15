def prod_signs(arr):
    if not arr:
        return None

    sign_product = 1
    zero_present = False
    magnitude_sum = 0

    for num in arr:
        if num < 0:
            sign_product *= -1
        elif num == 0:
            zero_present = True

        magnitude_sum += abs(num)

    if zero_present:
        return 0
    else:
        return sign_product * magnitude_sum
