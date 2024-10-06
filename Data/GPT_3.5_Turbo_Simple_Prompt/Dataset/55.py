def fib(n: int):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Test the function with the given examples
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
