def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',', ' ').split()
    else:
        return len([char for char in txt if char.islower() and ord(char) % 2 == 0])
