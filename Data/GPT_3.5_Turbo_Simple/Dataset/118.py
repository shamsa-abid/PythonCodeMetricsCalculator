def get_closest_vowel(word):
    vowels = "aeiouAEIOU"

    for i in range(len(word)-3, 0, -1):
        if word[i] in vowels:
            return word[i]

    return ""
