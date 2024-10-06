def get_odd_collatz(n):
    # Initialize a list to store the odd numbers in the Collatz sequence
    odd_numbers = []

    # Iterate through each number in the Collatz sequence starting from n
    while n != 1:
        if n % 2 == 1:
            odd_numbers.append(n)
        n = n * 3 + 1 if n % 2 else n // 2

    # Append the final number (1) if it is odd
    if n == 1:
        odd_numbers.append(n)

    # Sort and return the list of odd numbers
    return sorted(odd_numbers)


# Test the function with an example
print(get_odd_collatz(5))  # Output: [1, 5]
