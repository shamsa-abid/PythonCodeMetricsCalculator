def largest_prime_factor(n: int):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                return False
        return True

    largest = 1
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0 and is_prime(j):
            largest = j

    return largest


METADATA = {}
