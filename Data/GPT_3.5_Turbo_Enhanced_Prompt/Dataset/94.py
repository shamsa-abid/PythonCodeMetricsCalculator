def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


def find_largest_prime_sum(lst):
    max_prime = max(filter(is_prime, lst), default=0)
    return sum_of_digits(max_prime)
