def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    groups = []
    for c in paren_string:
        if c == ' ':
            continue
        if c == '(':
            stack.append(c)
        elif c == ')':
            message = ''
            while stack[-1] != '(':
                message = stack.pop() + message
            stack.pop()
            message = '(' + message + ')'
            if len(stack) > 0 and stack[-1] != '(':
                stack[-1] += message
            else:
                stack.append(message)
    while len(stack) > 0:
        groups.append(stack.pop())
    return groups[::-1]
