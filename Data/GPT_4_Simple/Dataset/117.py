def select_words(s, n):
    vowels = 'aeiou'
    s = s.split(' ')
    result = []

    for word in s:
        consonants = sum([1 for char in word if char.lower() not in vowels])
        if consonants == n:
            result.append(word)

    return result
