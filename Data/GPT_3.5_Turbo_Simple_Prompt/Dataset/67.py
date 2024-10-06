def fruit_distribution(s, n):
    apples = 0
    oranges = 0

    # Extract the number of apples and oranges from the input string
    for char in s.split():
        if char.isnumeric():
            if "apples" in s:
                apples = int(char)
            elif "oranges" in s:
                oranges = int(char)

    # Calculate the number of mango fruits
    mango = n - apples - oranges

    return mango


# Test the function with the given examples
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
