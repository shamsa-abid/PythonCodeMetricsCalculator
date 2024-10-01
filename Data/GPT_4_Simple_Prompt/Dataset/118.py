def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    result = ''
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels:
            if word[i-1] not in vowels and i+1 < len(word) and word[i+1] not in vowels:
                result = word[i]
                break
    return result
