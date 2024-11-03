def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False

    last_char = txt.strip()[-1]
    return last_char.isalpha() and last_char not in set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
