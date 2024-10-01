def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == "[":
            stack.append(bracket)
        elif bracket == "]":
            if not stack:
                return False
            stack.pop()
    return False if stack else True
