def is_bored(S):
    boredom_count = 0
    sentences = S.split('. ') + S.split('? ') + S.split('! ')

    for sentence in sentences:
        words = sentence.split()
        if len(words) > 0 and words[0] == "I":
            boredom_count += 1

    return boredom_count
