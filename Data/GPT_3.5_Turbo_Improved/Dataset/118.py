def get_closest_vowel(word):
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u"}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and not (word[i+1] in vowels or word[i-1] in vowels):
            return word[i]

    return ""
