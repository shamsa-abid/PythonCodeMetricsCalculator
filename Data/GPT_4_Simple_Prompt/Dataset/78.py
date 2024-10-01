def hex_key(num):
    """
    Rceives a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes.
    """
    primes_in_hex = ['2', '3', '5', '7', 'B', 'D']
    return sum(1 for i in num if i in primes_in_hex)
