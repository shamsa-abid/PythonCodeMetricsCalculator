def find_max(words):
    sorted_unique_chars = sorted(words, key=lambda x: (-len(set(x)), x))
    return sorted_unique_chars[0]
