
def encode(message):
    encoded_message = ""
    vowels = 'AEIOUaeiou'

    for char in message:
        if char.isalpha():
            if char in vowels:
                index = ord(char) + 2
                if char.isupper():
                    if index > ord('Z'):
                        index -= 26
                else:
                    if index > ord('z'):
                        index -= 26
                encoded_message += chr(index)
            else:
                if char.isupper():
                    encoded_message += char.lower()
                else:
                    encoded_message += char.upper()
        else:
            encoded_message += char

    return encoded_message
