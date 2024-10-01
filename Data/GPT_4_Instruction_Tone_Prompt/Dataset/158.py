def find_max(words):
    words.sort()
    max_word = words[0]
    max_count = len(set(words[0]))
    for word in words[1:]:
        count = len(set(word))
        if count > max_count:
            max_count = count
            max_word = word
    return max_word
