def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:  # stack is empty, means no matching open bracket
                return False
            stack.pop()  # pop the matching open bracket
    return False if stack else True  # return False if there are unmatched open brackets
