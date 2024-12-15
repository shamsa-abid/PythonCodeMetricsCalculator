def anti_shuffle(s):
    return ' '.join(sorted(i) if i.isalpha() else i for i in s.split(' '))
