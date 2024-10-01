
def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = max(filter(is_prime, lst), default=0)
    return sum(int(digit) for digit in str(largest_prime))
