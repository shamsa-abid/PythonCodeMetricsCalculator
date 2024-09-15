def correct_bracketing(brackets: str):
    opening_brackets = 0
    for b in brackets:
        if b == "<":
            opening_brackets += 1
        else:
            if opening_brackets == 0:
                return False
            opening_brackets -= 1
    return opening_brackets == 0
