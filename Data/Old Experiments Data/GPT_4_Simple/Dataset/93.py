def encode(message):
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'm', 'u': 'w',
              'A': 'C', 'E': 'G', 'I': 'K', 'O': 'M', 'U': 'W'}
    result = ""
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                result += vowels[letter]
            else:
                result += chr(ord(letter) ^ 32)
        else:
            result += letter
    return result
