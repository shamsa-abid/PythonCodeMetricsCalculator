def anti_shuffle(s):
    return ' '.join(map(lambda word: ''.join(sorted(word)), s.split(' ')))
