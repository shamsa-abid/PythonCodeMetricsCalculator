def multiply(a, b):
    a = abs(a)
    b = abs(b)
    a_unit = a % 10
    b_unit = b % 10
    return a_unit * b_unit
