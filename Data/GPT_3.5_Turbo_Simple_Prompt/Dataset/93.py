def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''

    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_message += chr(ord(char) + 2).swapcase()
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char

    return encoded_message


# Test cases
print(encode('test'))  # Output: TGST
print(encode('This is a message'))  # Output: tHKS KS C MGSSCGG
