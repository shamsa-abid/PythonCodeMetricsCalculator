def largest_prime_factor(n: int):
    def is_prime(k):
        if k < 2:
            return False
        if k == 2:
            return True
        if k % 2 == 0:
            return False
        for i in range(3, int(k**0.5) + 1, 2):
            if k % i == 0:
                return False
        return True

    largest = 1
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            if is_prime(j):
                largest = max(largest, j)
            if is_prime(n // j):
                largest = max(largest, n // j)

    return largest
