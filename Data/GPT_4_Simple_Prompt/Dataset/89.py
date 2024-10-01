def encrypt(s):
    result = ''
    for char in s:
        # Check if character is an alphabet
        if char.isalpha():
            # Check for special case of last two characters ('y' and 'z')
            if ord(char) >= ord('y'):
                result += chr(ord(char) - 24)
            else:
                result += chr(ord(char) + 4)
        else:
            result += char
    return result
