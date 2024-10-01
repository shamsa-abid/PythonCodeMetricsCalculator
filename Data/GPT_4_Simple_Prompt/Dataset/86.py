def anti_shuffle(s):
    # split string into words
    words = s.split(' ')

    # order characters in each word
    ordered_words = [''.join(sorted(word)) for word in words]

    # join ordered words back into a string
    s_ordered = ' '.join(ordered_words)

    return s_ordered
