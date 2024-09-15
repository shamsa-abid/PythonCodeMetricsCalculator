def select_words(s, n):
    vowels = set("aeiouAEIOU")
    return [word for word in s.split() if sum(letter not in vowels for letter in word) == n]
