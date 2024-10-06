
def special_factorial(n):
    result = 1
    for i in range(1, n+1):
        factorial = 1
        for j in range(1, i+1):
            factorial *= j
        result *= factorial
    return result


# Test the function with an example
print(special_factorial(4))  # Output: 288
