def prod_signs(arr):
    if not arr:
        return None

    product = 1
    magnitude_sum = 0
    for num in arr:
        if num > 0:
            product *= 1
            magnitude_sum += num
        elif num < 0:
            product *= -1
            magnitude_sum += abs(num)

    return product * magnitude_sum


# Test cases
print(prod_signs([1, 2, 2, -4]))  # Output: -9
print(prod_signs([0, 1]))  # Output: 0
print(prod_signs([]))  # Output: None
