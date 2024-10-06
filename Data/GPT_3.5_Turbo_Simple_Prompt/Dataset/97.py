def multiply(a, b):
    return int(str(abs(a))[-1]) * int(str(abs(b))[-1])


# Test cases
print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))  # Output: 72
print(multiply(2020, 1851))  # Output: 0
print(multiply(14, -15))  # Output: 20
