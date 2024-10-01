
def largest_divisor(n: int) -> int:
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return i


# Test the function with the example given in the docstring
print(largest_divisor(15))  # Output: 5
