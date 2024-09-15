from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = ''
    paren_count = 0

    for char in paren_string.replace(' ', ''):
        if char == '(':
            paren_count += 1
        elif char == ')':
            paren_count -= 1
        current_string += char

        if paren_count == 0:
            result.append(current_string)
            current_string = ''

    return result
