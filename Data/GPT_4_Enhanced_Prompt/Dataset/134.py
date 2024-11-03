def check_if_last_char_is_a_letter(txt):
    last_word = txt.rstrip().split(' ')[-1]
    return last_word.isalpha() and len(last_word) == 1
