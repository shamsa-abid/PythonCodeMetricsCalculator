def find_max(words):
    def unique_chars(word):
        return len(set(word))

    max_word = ""
    max_unique_chars = 0

    for word in words:
        curr_unique_chars = unique_chars(word)
        if curr_unique_chars > max_unique_chars:
            max_word = word
            max_unique_chars = curr_unique_chars
        elif curr_unique_chars == max_unique_chars:
            max_word = min(max_word, word)

    return max_word
