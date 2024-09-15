def check_if_last_char_is_a_letter(txt):
    txt = txt.strip()
    return txt and txt[-1].isalpha() and not txt[-1].isalnum()
