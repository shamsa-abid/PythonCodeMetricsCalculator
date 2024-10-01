def words_string(s):
    words = []
    for word in s.replace(',', ' ').split():
        words.append(word)
    return words
