def anti_shuffle(s):
    return ' '.join([''.join(sorted(i)) for i in s.split(' ')])
