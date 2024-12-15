def remove_vowels(text):
    vowels = set("aeiouAEIOU")
    return ''.join([character for character in text if character not in vowels])
