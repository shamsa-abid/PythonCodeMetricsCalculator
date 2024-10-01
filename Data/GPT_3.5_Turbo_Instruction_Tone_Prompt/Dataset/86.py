
def anti_shuffle(s):
    words = s.split()
    ordered_words = []

    for word in words:
        letters = sorted(word)
        ordered_words.append(''.join(letters))

    return ' '.join(ordered_words)
