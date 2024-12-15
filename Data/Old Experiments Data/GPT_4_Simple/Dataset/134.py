def check_if_last_char_is_a_letter(txt):
    if not txt:  # an empty string
        return False
    if txt[-1].isspace():  # the last char is a space
        return False
    if txt[-1].isalpha():  # the last char is an alphabet
        if txt[-2].isspace():  # the second last char is a space
            return True
    return False
