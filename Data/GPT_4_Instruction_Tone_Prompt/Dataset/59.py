def largest_prime_factor(n: int):
    prime_factor = 1
    i = 2
    while i <= n / i:
        if n % i:
            i += 1
        else:
            n /= i
            prime_factor = i
    if n > 1:
        prime_factor = n
    return int(prime_factor)
