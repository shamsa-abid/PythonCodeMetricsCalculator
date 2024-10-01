def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return len([x for x in txt if (ord(x.lower())-97) % 2 != 0])

