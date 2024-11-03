def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum(1 for char in txt if char.islower() and (ord(char)-ord('a')) % 2 != 0)
