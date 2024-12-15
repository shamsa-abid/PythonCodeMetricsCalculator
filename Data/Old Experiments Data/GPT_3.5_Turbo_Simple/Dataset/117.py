def select_words(s, n):
    def count_consonants(word):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        count = 0
        for char in word:
            if char in consonants:
                count += 1
        return count

    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)

    return result
