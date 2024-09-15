def encrypt(s):
    res = ''
    for i in s:
        res += chr((ord(i)-97+4) % 26+97)
    return res
