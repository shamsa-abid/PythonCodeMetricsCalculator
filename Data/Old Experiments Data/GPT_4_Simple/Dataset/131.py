def digits(n):
    p = 1
    no_odd_digits = True
    for digit in str(n):
        digit = int(digit)
        if digit % 2 != 0:
            p *= digit
            no_odd_digits = False
    return 0 if no_odd_digits else p
