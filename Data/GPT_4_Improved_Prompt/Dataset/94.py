def skjkasdkd(lst):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [n for n in lst if isPrime(n)]
    if prime_numbers:
        largest_prime = max(prime_numbers)
        return sum(map(int, str(largest_prime)))
    else:
        return 0
