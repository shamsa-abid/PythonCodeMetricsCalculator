def prime_length(string):
    # Check if number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Calculate string length
    length = len(string)

    # Return if length is prime
    return is_prime(length)
