def largest_prime_factor(n: int):
    def is_prime(x):
        if x <= 1:
            return False
        elif x <= 3:
            return True
        elif x % 2 == 0 or x % 3 == 0:
            return False
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i += 6
        return True

    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    if n > 1 and is_prime(n):
        return n
    else:
        return i
