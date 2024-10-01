def anti_shuffle(s):
    words = s.split(' ')
    ordered_words = [''.join(sorted(word)) for word in words]
    ordered_s = ' '.join(ordered_words)
    return ordered_s
