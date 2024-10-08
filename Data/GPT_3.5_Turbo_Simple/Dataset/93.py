def encode(message):
    result = ""
    vowels = "AEIOUaeiou"

    for char in message:
        if char.isalpha():
            if char.upper() in vowels:
                new_char = chr(ord(char) + 2)
            else:
                new_char = char.swapcase()
            result += new_char
        else:
            result += char

    return result
