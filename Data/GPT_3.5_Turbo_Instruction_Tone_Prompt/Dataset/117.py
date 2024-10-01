def select_words(s, n):
    def count_consonants(word):
        vowels = "aeiouAEIOU"
        return sum(1 for letter in word if letter.isalpha() and letter not in vowels)

    words = s.split()
    return [word for word in words if count_consonants(word) == n] if s else []
