
def encode(message):
    import string
    vowels = "aeiouAEIOU"
    vowels_replace = {v: chr(ord(v) + 2) for v in vowels}
    message = message.swapcase()
    return ''.join(vowels_replace.get(i, i) for i in message)
