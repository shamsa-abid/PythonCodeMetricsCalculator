def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    word = word[::-1]  # Reversing the word to search from right side

    for i in range(len(word)):
        if word[i] in vowels:
            before = word[i-1] if i > 0 else ''
            after = word[i+1] if i < len(word)-1 else ''

            if before in consonants and after in consonants:
                return word[i]

    return ""
