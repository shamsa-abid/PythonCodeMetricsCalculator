def encrypt(s):
    return ''.join(chr((ord(char) - 97 + 4) % 26 + 97) if char.islower() else char for char in s)
