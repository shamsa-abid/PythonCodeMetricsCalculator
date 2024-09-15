def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sum_of_digits(n):
    return sum(int(x) for x in str(n))


def skjkasdkd(lst):
    # get a list of primes then find max in the list and then sum its digits
    max_prime = max(filter(is_prime, lst))
    return sum_of_digits(max_prime)
