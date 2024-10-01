def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Parameters:
    n (int): The number up to which the sum of numbers is calculated.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    return n * (n + 1) // 2


# Testing the function with given test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
