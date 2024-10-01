from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    paren_string = paren_string.replace(' ', '')
    parentheses_balance = left_parenthesis_index = 0

    for index, character in enumerate(paren_string):
        if character == '(':
            if parentheses_balance == 0:
                left_parenthesis_index = index
            parentheses_balance += 1
        elif character == ')':
            parentheses_balance -= 1
            if parentheses_balance == 0:
                result.append(paren_string[left_parenthesis_index:index+1])

    return result
