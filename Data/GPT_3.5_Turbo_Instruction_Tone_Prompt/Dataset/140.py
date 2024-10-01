def fix_spaces(text):
    fixed_text = ""
    consecutive_spaces = 0

    for char in text:
        if char == " ":
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                fixed_text = fixed_text.rstrip("-") + "-"
        else:
            if consecutive_spaces > 2:
                fixed_text += "-"
            elif consecutive_spaces > 0:
                fixed_text += "_"
            fixed_text += char
            consecutive_spaces = 0

    if consecutive_spaces > 2:
        fixed_text = fixed_text.rstrip("-") + "-"
    elif consecutive_spaces > 0:
        fixed_text += "_"

    return fixed_text
