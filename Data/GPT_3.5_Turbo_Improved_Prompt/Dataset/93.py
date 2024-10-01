
def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = {i: chr(ord(i) + 2) for i in vowels}
    message = message.swapcase()
    encoded_message = ''.join([vowels_replace.get(i, i) for i in message])
    return encoded_message
