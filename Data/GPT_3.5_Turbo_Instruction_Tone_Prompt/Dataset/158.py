def find_max(words):
    def unique_chars(word):
        return len(set(word))

    max_word = ""
    max_unique_chars = 0

    for word in words:
        unique = unique_chars(word)
        if unique > max_unique_chars or (unique == max_unique_chars and word < max_word):
            max_words = word
            max_unique_chars = unique

    return max_word
