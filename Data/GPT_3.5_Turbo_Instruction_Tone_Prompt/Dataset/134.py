
def check_if_last_char_is_a_letter(txt):
    if txt == "":
        return False
    elif txt[-1].isalpha() and (len(txt) == 1 or not txt[-2].isalpha()):
        return True
    else:
        return False
