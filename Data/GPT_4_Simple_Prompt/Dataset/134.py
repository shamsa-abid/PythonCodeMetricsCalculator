def check_if_last_char_is_a_letter(txt):
    return txt[-2] == " " and txt[-1].isalpha() if len(txt) > 1 else False
