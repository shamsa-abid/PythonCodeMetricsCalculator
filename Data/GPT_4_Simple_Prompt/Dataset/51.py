def remove_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return ''.join([letter for letter in text if letter not in vowels])
