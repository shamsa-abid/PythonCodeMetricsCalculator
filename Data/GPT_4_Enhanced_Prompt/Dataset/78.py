def hex_key(num):
    primes = set('2357BD')
    return sum(1 for digit in num if digit in primes)
