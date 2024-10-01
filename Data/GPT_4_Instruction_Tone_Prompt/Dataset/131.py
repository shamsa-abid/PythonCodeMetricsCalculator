def digits(n):
    n = str(n)
    prod = 1
    for digit in n:
        if int(digit) % 2 != 0:
            prod *= int(digit)
    return prod if prod != 1 else 0
