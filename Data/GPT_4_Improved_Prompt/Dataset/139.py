def special_factorial(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Please provide a positive integer value')

    product = 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        product *= factorial
    return product
