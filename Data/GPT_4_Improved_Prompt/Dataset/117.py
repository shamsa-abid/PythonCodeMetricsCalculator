def select_words(s, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [word for word in s.split() if sum(1 for char in word if char.lower() not in vowels) == n]
