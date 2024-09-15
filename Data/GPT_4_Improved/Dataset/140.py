def fix_spaces(text):
    new_text = ''
    space_count = 0

    for char in text:
        if char == ' ':
            space_count += 1
        else:
            new_text += '-' * max(space_count//3, 0)
            new_text += '_' * (space_count % 3)
            new_text += char
            space_count = 0

    new_text += '-' * max(space_count//3, 0)
    new_text += '_' * (space_count % 3)
    return new_text
