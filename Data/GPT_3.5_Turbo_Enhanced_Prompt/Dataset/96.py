def count_up_to(n):
    if n < 2:
        return []

    primes = [2]
    for i in range(3, n, 2):
        is_prime = True
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes

# The above implementation takes advantage of the following optimizations:
# - Only checking odd numbers after 2 since even numbers greater than 2 are not prime
# - Only checking up to the square root of the current number, as any factor larger than the square root will have a corresponding factor smaller than the square root
# - Checking for factors only in odd numbers, as even factors were eliminated in the first step
# This results in better performance and readability compared to the initial solution.
