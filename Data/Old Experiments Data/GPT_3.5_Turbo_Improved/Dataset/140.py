def fix_spaces(text):
    new_text = ""
    consecutive_spaces = 0

    for char in text:
        if char == " ":
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                new_text += "-"
            else:
                new_text += "_"
        else:
            new_text += char
            consecutive_spaces = 0

    return new_text
