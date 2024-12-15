def encrypt(s):
    encrypted = ""
    for char in s:
        if char.isalpha():
            shift = 2 * ord(char) - 2
            if char.islower():
                encrypted += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                encrypted += chr(((ord(char) - 65 + shift) % 26) + 65)
        else:
            encrypted += char
    return encrypted
