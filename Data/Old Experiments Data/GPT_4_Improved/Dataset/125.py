def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return len([ch for ch in txt if ch.islower() and (ord(ch) - ord('a')) % 2 != 0])
