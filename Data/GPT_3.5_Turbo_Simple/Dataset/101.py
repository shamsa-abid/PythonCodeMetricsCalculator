def words_string(s):
    words = [word.strip() for word in s.replace(",", " ").split()]
    return words
