def encrypt(s):
    encrypted = ""
    for char in s:
        if char.isalpha():
            shift = (ord(char) - ord('a') + 2) % 26
            encrypted += chr(ord('a') + shift)
        else:
            encrypted += char
    return encrypted
