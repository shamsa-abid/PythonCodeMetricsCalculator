def add_elements(arr, k):
    sum_two_digits = 0
    count = 0

    for num in arr[:k]:
        if 10 <= abs(num) <= 99:
            sum_two_digits += num
            count += 1

    return sum_two_digits
