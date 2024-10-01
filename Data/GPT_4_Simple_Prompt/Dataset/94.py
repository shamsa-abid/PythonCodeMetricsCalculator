def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_nums = [num for num in lst if is_prime(num)]
    if prime_nums:
        return sum([int(digit) for digit in str(max(prime_nums))])
    else:
        return 0
