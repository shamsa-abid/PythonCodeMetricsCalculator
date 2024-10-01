def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def hex_key(num):
    prime_digits = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit.upper() in prime_digits:
            count += 1
    return count


# Test cases
print(hex_key("AB"))  # Output: 1
print(hex_key("1077E"))  # Output: 2
print(hex_key("ABED1A33"))  # Output: 4
print(hex_key("123456789ABCDEF0"))  # Output: 6
print(hex_key("2020"))  # Output: 2
