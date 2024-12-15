def special_factorial(n):
    output = 1
    accumulator = 1
    for i in range(1, n+1):
        accumulator *= i
        output *= accumulator
    return output
