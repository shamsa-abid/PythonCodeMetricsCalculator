def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqr = int(n**0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    p_max = max(filter(is_prime, lst), default=0)
    return sum(map(int, str(p_max)))
