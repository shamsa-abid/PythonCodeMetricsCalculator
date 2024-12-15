def multiply(a, b):
    return (a % 10) * (b % 10) if (isinstance(a, int) and isinstance(b, int)) else "Error: Input should be integer"
