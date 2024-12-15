def fix_spaces(text):
    text = text.replace(" ", "_")

    i = 0
    result = ""
    while i < len(text):
        if text[i] == " ":
            count = 0
            while i < len(text) and text[i] == " ":
                count += 1
                i += 1

            if count > 2:
                result += "-"
            else:
                result += "_"
        else:
            result += text[i]
            i += 1

    return result
