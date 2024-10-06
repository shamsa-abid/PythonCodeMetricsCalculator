
def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if stack[-1] == '(':
                stack.pop()
                if len(stack) == 0:
                    result.append(''.join(stack))
            else:
                stack.append(')')

    return result
