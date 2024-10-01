def check_if_last_char_is_a_letter(txt):
    # strip the spaces from the end of the string
    txt = txt.rstrip()
    # if the string is empty after stripping, return False
    if not txt:
        return False

    # check the last character in the string
    last_char = txt[-1]
    # if the last character is a letter return True only if it has a space or it is a single letter
    if last_char.isalpha():
        if len(txt) == 1 or txt[-2] == ' ':
            return True
    return False
