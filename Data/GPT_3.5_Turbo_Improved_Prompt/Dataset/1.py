
def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = ""
    current_depth = 0

    for c in paren_string.replace(" ", ""):
        if c == '(':
            current_depth += 1
            current_string += c
        elif c == ')':
            current_depth -= 1
            current_string += c

            if current_depth == 0:
                result.append(current_string)
                current_string = ""

    return result
