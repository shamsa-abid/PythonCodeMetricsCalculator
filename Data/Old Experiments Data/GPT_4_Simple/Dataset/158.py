def find_max(words):
    unique_chars_num = [len(set(word)) for word in words]
    max_unique_chars = max(unique_chars_num)
    words_max_unique = [word for word in words if len(
        set(word)) == max_unique_chars]
    return min(words_max_unique)
