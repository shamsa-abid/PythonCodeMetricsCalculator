def words_string(s):
    if not s:
        return []

    words = s.replace(',', ' ').split()

    return words
