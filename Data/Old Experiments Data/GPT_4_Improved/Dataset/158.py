def find_max(words):
    words.sort()
    return max(words, key=lambda x: len(set(x)))
