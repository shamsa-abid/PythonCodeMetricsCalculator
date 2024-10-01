def encode(message):
    result = ''
    vowels = 'aeiou'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for char in message:
        # If char is a vowel, replace with letter 2 places ahead in alphabet
        if char.lower() in vowels:
            char_index = alpha.index(char.lower())
            if char.isupper():
                result += alpha[(char_index + 2) % 26].upper()
            else:
                result += alpha[(char_index + 2) % 26]
        # If char is a letter, but not a vowel, simply swap case
        elif char.isalpha():
            result += char.swapcase()
        # If char is not a letter (like space), just append it to result
        else:
            result += char
    return result