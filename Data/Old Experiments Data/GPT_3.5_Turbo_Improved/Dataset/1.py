from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = []

    for c in paren_string:
        if c == '(':
            current_string.append(c)
        elif c == ')':
            current_string.append(c)
            if c == ' ':
                current_string.pop()
            else:
                result.append(''.join(current_string))
                current_string = []

    return result
