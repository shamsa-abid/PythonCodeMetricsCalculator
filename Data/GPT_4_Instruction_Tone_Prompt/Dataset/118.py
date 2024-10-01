def get_closest_vowel(word):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    word = word[::-1]
    for char in word:
        if char in vowels and word[word.index(char)+1].isalpha() and word[word.index(char)+2].isalpha():
            return char
    return ""
