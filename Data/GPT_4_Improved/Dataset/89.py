def encrypt(s):
    return "".join([chr((ord(c)-97+4) % 26+97) if c.isalpha() else c for c in s])
