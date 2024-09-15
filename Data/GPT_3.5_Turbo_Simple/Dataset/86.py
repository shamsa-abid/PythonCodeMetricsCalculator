def anti_shuffle(s):
    def order_string(word):
        return ''.join(sorted(word))

    ordered_sentence = []
    words = s.split()
    for word in words:
        ordered_sentence.append(order_string(word))

    return ' '.join(ordered_sentence)
