def hex_key(num):
    prime_hex_chars = ['2', '3', '5', '7', 'B', 'D']
    return sum(char in prime_hex_chars for char in num)
