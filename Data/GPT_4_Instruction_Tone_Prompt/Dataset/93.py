def encode(message):
    vowels = 'aeiouAEIOU'
    encoded = ''

    for char in message:
        if char.isalpha():
            new_char = char
            if char in vowels:
                new_char = chr(ord(char) + 2)
                # Handle vowels at end of alphabet
                if new_char in ('{', '['):
                    new_char = chr(ord(char) - 24)
            encoded += new_char.swapcase()
        else:
            encoded += char

    return encoded
