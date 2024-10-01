def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # this function returns true if number is prime and false otherwise
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # creating the list of prime numbers upto 100
    primes = [x for x in range(2, 101) if is_prime(x)]

    # checking product of all possible combinations of 3 primes
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True

    return False
