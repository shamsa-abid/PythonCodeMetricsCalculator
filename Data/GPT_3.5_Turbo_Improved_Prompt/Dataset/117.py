def select_words(s, n):
    result = []
    vowels = set(['a', 'e', 'i', 'o', 'u'])

    for word in s.split():
        n_consonants = sum(
            1 for letter in word if letter.lower() not in vowels)
        if n_consonants == n:
            result.append(word)

    return result
