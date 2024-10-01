def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    words = s.split(' ')
    selected = []
    for word in words:
        count = sum([1 for char in word if char in consonants])
        if count == n:
            selected.append(word)
    return selected
