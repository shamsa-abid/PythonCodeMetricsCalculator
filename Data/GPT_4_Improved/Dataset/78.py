def hex_key(num):
    primes = set('2357BD')
    return sum(el in primes for el in num)
