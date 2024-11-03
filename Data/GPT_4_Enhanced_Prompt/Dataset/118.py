def get_closest_vowel(word):
    if len(word) < 3:
        return ""

    vowels = set("aeiouAEIOU")
    for i in range(len(word)-2, -1, -1):
        if word[i] in vowels and word[i+1] not in vowels and word[i-1] not in vowels:
            return word[i]
    return ""
