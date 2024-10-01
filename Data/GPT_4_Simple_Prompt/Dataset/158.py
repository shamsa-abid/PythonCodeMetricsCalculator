def find_max(words):
    max_len = max([len(set(word)) for word in words])
    words_with_max_unique_chars = [
        word for word in words if len(set(word)) == max_len]
    return min(words_with_max_unique_chars)
