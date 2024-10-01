def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    result = []
    current_group = ''
    open_parentheses = 0

    for char in paren_string:
        if char == '(':
            open_parentheses += 1
        elif char == ')':
            open_parentheses -= 1

        current_group += char
        if open_parentheses == 0:
            result.append(current_group)
            current_group = ''

    return result
