def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_val = ord(char)
            new_ascii_val = ascii_val + 2 * 2  # shift down by two multiplied to two places
            if char.islower():
                if new_ascii_val > ord('z'):
                    new_ascii_val -= 26
            elif char.isupper():
                if new_ascii_val > ord('Z'):
                    new_ascii_val -= 26
            result += chr(new_ascii_val)
        else:
            result += char
    return result


# Testing the function with examples
print(encrypt('hi'))  # 'lm'
print(encrypt('asdfghjkl'))  # 'ewhjklnop'
print(encrypt('gf'))  # 'kj'
print(encrypt('et'))  # 'ix'
