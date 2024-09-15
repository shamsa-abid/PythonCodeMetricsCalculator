def check_if_last_char_is_a_letter(txt):
    if txt == "":
        return False
    last_char = txt.strip()[-1]
    if last_char.isalpha() and not last_char.isspace():
        return True
    return False
