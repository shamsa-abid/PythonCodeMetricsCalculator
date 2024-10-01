def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    a, b, c, d = 0, 0, 2, 0

    for i in range(4, n+1):
        result = a + b + c + d
        a, b, c, d = b, c, d, result

    return result


# Testing the function with the given test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
