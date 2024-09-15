def count_up_to(n):
    if n <= 2:
        return []
    primes = [2]
    for num in range(3, n):
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
    return primes
