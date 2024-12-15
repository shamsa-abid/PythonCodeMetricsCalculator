def special_factorial(n):
    result = 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        result *= factorial
    return result
