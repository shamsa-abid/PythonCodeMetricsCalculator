def digits(n):
    result = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            result *= int(digit)

    if result == 1:
        return 0
    else:
        return result


# Test cases
print(digits(1))    # Output: 1
print(digits(4))    # Output: 0
print(digits(235))  # Output: 15
