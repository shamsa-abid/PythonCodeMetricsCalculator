def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    new_word = word[::-1]
    for i in range(1, len(new_word) - 1):
        if new_word[i] in vowels and new_word[i-1] not in vowels and new_word[i+1] not in vowels:
            return new_word[i]
    return ''
