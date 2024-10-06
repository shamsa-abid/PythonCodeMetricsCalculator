def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Test cases
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441))  # True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
