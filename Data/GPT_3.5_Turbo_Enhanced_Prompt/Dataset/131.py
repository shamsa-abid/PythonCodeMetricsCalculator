def digits(n):
    product = 1
    for digit in str(n):
        int_digit = int(digit)
        if int_digit % 2 != 0:
            product *= int_digit
    return product if product != 1 else 0  # Return 0 if all digits are even
