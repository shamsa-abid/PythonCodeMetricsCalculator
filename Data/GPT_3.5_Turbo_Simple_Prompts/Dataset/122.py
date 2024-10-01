def add_elements(arr, k):
    sum = 0
    count = 0

    for num in arr[:k]:
        if 10 <= num < 100:
            sum += num
            count += 1

    return sum


# Test the function with the given example
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
print(add_elements(arr, k))  # Output: 24
