def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False

    last_chars = txt.rstrip().split(' ')[-1]

    return last_chars.isalpha() and len(last_chars) == 1
