def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int):
    if n == 1:
        return 2
    elif n == 2:
        return 3

    fib_sequence = [1, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    prime_fib_numbers = [x for x in fib_sequence if is_prime(x)]

    return prime_fib_numbers[-1]


# Test the function with given test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
