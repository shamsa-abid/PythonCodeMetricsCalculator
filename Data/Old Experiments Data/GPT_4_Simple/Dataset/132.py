def is_nested(string):
    stack = []
    closed_outer_bracket = 0
    for i in string:
        if i == '[':
            stack.append(i)
        elif i == ']':
            if stack:
                stack.pop()
            else:
                closed_outer_bracket += 1
    return len(stack) == closed_outer_bracket and closed_outer_bracket > 0
