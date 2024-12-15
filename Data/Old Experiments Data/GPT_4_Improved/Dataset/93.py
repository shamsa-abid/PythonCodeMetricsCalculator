def encode(message):
    message = list(message.swapcase())
    for idx, char in enumerate(message):
        if char.lower() in 'aeiou':
            message[idx] = chr(ord(char) + 2)
    return ''.join(message)
